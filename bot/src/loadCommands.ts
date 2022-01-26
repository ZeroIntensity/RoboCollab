import fs from "fs";
import { Commands } from "./types";
import { CommandsDirectory } from "./constants";

export default function () {
	const commands: Commands = {};
	const commandFiles = fs
		.readdirSync(CommandsDirectory)
		.filter(file => file.endsWith(".js"));

	commandFiles.forEach(file => {
		const command = require(`./commands/${file}`);
		commands[command.name] = {
			data: command.data,
			execute: command.execute,
		};
	});

	return commands;
}
