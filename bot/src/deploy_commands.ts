import { REST } from "@discordjs/rest";
import { Routes } from "discord-api-types/v9";
import { Commands } from "./types";

export default function (token: string, clientId: string, commands: Commands) {
	const rest = new REST({ version: "9" }).setToken(token);
	const cmds = Object.keys(commands).map(command => {
		return commands[command].data.toJSON();
	});

	rest
		.put(Routes.applicationCommands(clientId), { body: cmds })
		.then(() => console.log("Successfully registered application commands."))
		.catch(console.error);
}
