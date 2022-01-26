import { SlashCommandBuilder } from "@discordjs/builders";
import discord from "discord.js";
import { apiRequest, makeError, makeSuccess } from "../constants";

module.exports = {
	name: "createcollab",
	data: new SlashCommandBuilder()
		.addStringOption(option => {
			return option
				.setName("name")
				.setDescription("Name of the collab.")
				.setRequired(true);
		})
		.setName("createcollab")
		.setDescription("Creates a collab."),

	execute: async function execute(interaction: discord.CommandInteraction) {
		const json = await apiRequest(
			`mutation {
			createCollab(data: $data)
		  }`,
			{
				data: {
					name: interaction.options.getString("name"),
					server: interaction.guildId,
					host: interaction.user.id,
				},
			}
		);

		console.log(json);
		let resp: discord.MessageEmbed;
		let errors = json["errors"];

		if (errors) {
			resp = makeError(
				errors.length >= 2 ? "An internal error occured!" : errors[0]["message"]
			);
		} else {
			resp = makeSuccess("Collab was successfully created!", "Create Collab");
		}

		await interaction.reply({ embeds: [resp] });
	},
};
