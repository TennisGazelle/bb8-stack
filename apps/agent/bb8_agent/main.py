from __future__ import annotations

import argparse
import asyncio

from rich import print

from .graph import build_graph


async def run(goal: str, transport: str) -> None:
    graph = build_graph()
    result = await graph.ainvoke({"goal": goal, "transport": transport})
    print("[bold]BB-8 Milestone 0 cycle complete[/bold]")
    print(result)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the BB-8 agent loop")
    parser.add_argument("--goal", required=True, help="User goal for the robot agent")
    parser.add_argument("--transport", default="fake", help="fake, mcp-http, or stdio later")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    asyncio.run(run(args.goal, args.transport))


if __name__ == "__main__":
    main()
