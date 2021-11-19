import { Client, Intents } from "discord.js";
import dotenv from "dotenv";
import loadCommands from "./load_commands";
import deployCommands from "./deploy_commands";
import { BotId } from "./constants";

dotenv.config();
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });
const token = process.env.token!;
const commands = loadCommands();

client.once("ready", () => {
	console.log("Ready!");
});

client.on("interactionCreate", async interaction => {
	if (!interaction.isCommand()) return;

	const command = commands[interaction.commandName];

	if (!command) return;

	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		await interaction.reply({
			content: "There was an error while executing this command!",
			ephemeral: true,
		});
	}
});

client.login(token);
deployCommands(token, BotId, commands);
