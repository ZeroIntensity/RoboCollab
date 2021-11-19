import { GraphQLFetchBody } from "./types";
import fetch from "node-fetch";
import discord from "discord.js";

export const CommandsDirectory = __dirname + "/commands";
export const BotId = "754902431258771567";
export const ApiUrl = "http://localhost:5000/gql";
export function GraphQLBody(
	query: string,
	variables?: object
): GraphQLFetchBody {
	return {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ query, variables }),
	};
}
export async function apiRequest(
	query: string,
	variables?: object
): Promise<any> {
	const data = await fetch(ApiUrl, GraphQLBody(query, variables));
	return data.json();
}
export function makeEmbed(
	title: string,
	description: string,
	color: discord.ColorResolvable = "DEFAULT",
	fields?: discord.EmbedFieldData[]
) {
	const embed = new discord.MessageEmbed();
	embed.setTitle(title).setDescription(description).setColor(color);

	if (fields) {
		embed.addFields(fields);
	}

	return embed;
}

export function makeError(message: string) {
	return makeEmbed("Error", message, "RED");
}
export function makeSuccess(message: string, title: string = "Success") {
	return makeEmbed(title, message, [136, 255, 77]);
}
