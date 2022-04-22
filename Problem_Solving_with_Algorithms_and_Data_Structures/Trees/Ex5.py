-- FUNCTION: web_e_respectrb.w3586962_data(jsonb, text)

-- DROP FUNCTION IF EXISTS web_e_respectrb.w3586962_data(jsonb, text);

CREATE OR REPLACE FUNCTION web_e_respectrb.w36031375_data(
    _value jsonb,
    _name_mod text)
    RETURNS TABLE(idkart integer, num_pay text, datecr text, kkl text, forwhat text, kdoc text, org text, sum text, nds text) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
declare  
    _MOD_NAME CONSTANT text = 'w3586962_filter';  -- название модуля фильтра
  
     -- ПОЛЯ ФИЛЬТРА
    _date_from timestamptz         = pdb2_val_include_text( _MOD_NAME, 'date', '{value, 0}' );                   -- дата начала отсчета
    _date_to timestamptz           = pdb2_val_include_text( _MOD_NAME, 'date', '{value, 1}' );                   -- дата конца отсчета
    _id25001 int                   = pdb2_val_include_text( _MOD_NAME, 'id25001', '{value}' );                   -- фирма
  
begin

    -- если дата конца не введена, то она равняется текущему времени
    if _date_to is null then
        _date_to = current_timestamp;
    end if;
    
    -- если дата начала больше текущего времени, получаем алерт
    if _date_from is not null and _date_from > current_timestamp then
        raise '%', 'Ай, время начала не может быть больше текущего времени!';
    end if;
    
    perform pdb2_val_session( 'w3586962', '{date,0}', _date_from );
    perform pdb2_val_session( 'w3586962', '{date,1}', _date_to );
    perform pdb2_val_session( 'w3586962', '{id25001}', _id25001 );
    
    RETURN QUERY
        select 
            t300.idkart,
            (t300.object_data ->> 'Номер') as num_pay, 
            to_char((t300.object_data ->> 'Дата')::timestamptz, 'dd.mm.yy') as datecr, 
            (t300.object_data ->> 'Ккл') as kkl,
            (t300.object_data ->> 'ЗаЧто') as forwhat,
            (t300.object_data ->> 'Кдок') as kdoc,
            (t300.object_data ->> 'Орг') as org,
            (t300.object_data ->> 'Сумма') as sum,
            (t300.object_data ->> 'НДС') as nds,
        from t300
        where tp = 1
        and t300.dttmcl is null
        and t300.dttmcr between _date_from and _date_to
        and ( _id25001 is null or t300.id200 = _id25001 )
        order by t300.dttmcr;
        ---------------------------------------
end;
$BODY$;

ALTER FUNCTION web_e_respectrb.w3586962_data(jsonb, text)
    OWNER TO developer_michael;
