const invokeIf = (condition, fnTrue, fnFalse) =>
	condition ? fnTrue() : fnFalse();

const showWelcome = () => console.log("Welcome!!!");

const showUnathorized = () => console.log("Unathorized");

invokeIf(true, showWelcome, showUnathorized);
invokeIf(false, showWelcome, showUnathorized);

const userLogs = userName => message => console.log(`${userName} -> ${message}`);

const log = userLogs("grandpa23");

log("attemped to load 20 fake members");
getFakeMembers(20).then(
	members => log(`sucessfully loaded ${members.length} members`),
	error => log("encountered an error loading members")
);