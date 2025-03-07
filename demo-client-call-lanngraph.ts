import { Client } from "@langchain/langgraph-sdk";

console.log("Hello");
// const client = new Client({ apiUrl: "http://localhost:8123" });
const client = new Client({ apiUrl: "http://localhost:2024" }); // URL if you run langgraph dev
console.log(client);
// Using the graph deployed with the name "agent"
const assistantID = "personality_downloader_agent";
// create thread
const thread = await client.threads.create();
console.log(thread);

const input = {
  messages: [
    {
      role: "human",
      content: "mark cuban",
    },
  ],
};
console.log(input);
const streamResponse = client.runs.stream(thread["thread_id"], assistantID, {
  input,
  streamMode: "updates",
});

console.log(streamResponse);
for await (const chunk of streamResponse) {
  console.log(`Receiving new event of type: ${chunk.event}...`);
  console.log(chunk.data);
  console.log("\n\n");
}
