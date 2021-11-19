import { SlashCommandBuilder } from "@discordjs/builders";
export type Command = {
	data: SlashCommandBuilder;
	execute: Function;
};
export type Commands = {
	[key: string]: Command;
};
export type RequestHeaders = { [key: string]: string };
export type RequestMethod = "GET" | "POST" | "PUT" | "DELETE";
export type GraphQLFetchBody = {
	method: RequestMethod;
	headers: RequestHeaders;
	body: string;
};
