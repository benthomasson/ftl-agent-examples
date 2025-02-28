from smolagents.tools import Tool
from ftl_agent.tools import get_json_schema

import os
import faster_than_light as ftl
import asyncio
import shutil

dependencies = [
    "ftl_module_utils @ git+https://github.com/benthomasson/ftl_module_utils@main"
]


def display_tool(tool):
    prefix = f"TOOL [{tool.name}] "
    print(prefix, "=" * (shutil.get_terminal_size((80, 20))[0] - len(prefix) - 1))


def display_results(output):
    for name, results in output.items():
        if results.get("failed"):
            raise Exception(results.get("msg"))
        if results.get("changed"):
            print(f"changed: [{name}]")
        else:
            print(f"ok: [{name}]")
    print("")


class Service(Tool):
    name = "service"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, name: str, state: str) -> bool:
        """Manager a service

        Args:
            name: the name of the service
            state: one of started, restarted, or stopped

        Returns:
            boolean
        """
        display_tool(self)

        output = asyncio.run(
            ftl.run_module(
                self.state["inventory"],
                self.state["modules"],
                "service",
                module_args=dict(name=name, state=state),
                dependencies=dependencies,
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)


class LineInFile(Tool):
    name = "lineinfile"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, line: str, state: str, path: str, regexp: str = None) -> bool:
        """Add a line to a file

        Args:
            line: the line to add
            state: one of present or absent
            path: the path to the file
            regexp: the regular expression of the line to replace

        Returns:
            boolean
        """
        display_tool(self)
        output = asyncio.run(
            ftl.run_module(
                self.state["inventory"],
                self.state["modules"],
                "lineinfile",
                module_args=dict(line=line, state=state, path=path, regexp=regexp),
                dependencies=dependencies,
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)


class AuthorizedKey(Tool):
    name = "authorized_key"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, user: str, state: str, key: str) -> bool:
        """Manage authorized keys

        Args:
            user: the name of the user
            state: one of present or absent
            key: the path to the file containing the public key

        Returns:
            boolean
        """
        display_tool(self)
        key = os.path.abspath(os.path.expanduser(key))
        if not os.path.exists(key) or not os.path.isfile(key):
            raise Exception(f"{key} does not exist")
        with open(key) as f:
            key_value = f.read()
        output = asyncio.run(
            ftl.run_module(
                self.state["inventory"],
                self.state["modules"],
                "authorized_key",
                module_args=dict(user=user, state=state, key=key_value),
                dependencies=dependencies,
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)


class User(Tool):
    name = "user"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, name: str, group: str) -> bool:
        """Create a user

        Args:
            name: the name of the user
            group: the group the user should belong to

        Returns:
            boolean
        """
        display_tool(self)
        output = asyncio.run(
            ftl.run_module(
                self.state["inventory"],
                self.state["modules"],
                "user",
                module_args=dict(
                    name=name,
                    create_home=True,
                    group=group,
                ),
                dependencies=dependencies,
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)


class Dnf(Tool):
    name = "dnf"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, name: str, state: str) -> bool:
        """Control dnf packages

        Args:
            name: the name of the package, use '*' for all packages
            state: one of latest, present, absent

        Returns:
            boolean
        """
        display_tool(self)
        output = asyncio.run(
            ftl.run_module(
                self.state["inventory"],
                self.state["modules"],
                "dnf",
                module_args=dict(name=name, state=state),
                dependencies=dependencies,
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)


class Apt(Tool):
    name = "apt"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, update_cache: bool = False, upgrade: str = "no") -> bool:
        """Control apt packages

        Args:
            update_cache: Update the cache if true
            upgrade: Either yes, safe, or no.

        Returns:
            boolean
        """
        display_tool(self)
        output = asyncio.run(
            ftl.run_module(
                self.state["inventory"],
                self.state["modules"],
                "apt",
                module_args=dict(update_cache=update_cache, upgrade=upgrade),
                dependencies=dependencies,
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)


class Hostname(Tool):
    name = "hostname"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, name: str) -> bool:
        """Sets the hostname of the machine.

        Args:
            name: the name to set

        Returns:
            boolean
        """
        display_tool(self)
        output = asyncio.run(
            ftl.run_module(
                self.state["inventory"],
                self.state["modules"],
                "hostname",
                module_args=dict(name=name),
                dependencies=dependencies,
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)


class Slack(Tool):
    name = "slack"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, msg: str) -> bool:
        """Sends a message to slack.

        Args:
            msg: the message to send

        Returns:
            boolean
        """
        display_tool(self)
        output = asyncio.run(
            ftl.run_module(
                self.state["localhost"],
                self.state["modules"],
                "slack",
                module_args=dict(msg=msg, token=self.state["slack_token"]),
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)


class Discord(Tool):
    name = "discord"

    def __init__(self, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)

    def forward(self, message: str) -> bool:
        """Sends a message to discord.

        Args:
            message: the message to send

        Returns:
            boolean
        """
        display_tool(self)
        output = asyncio.run(
            ftl.run_module(
                self.state["localhost"],
                self.state["modules"],
                "discord",
                module_args=dict(
                    content=message,
                    webhook_token=self.state["discord_token"],
                    webhook_id=self.state["discord_channel"],
                ),
            )
        )

        display_results(output)

        return True

    description, inputs, output_type = get_json_schema(forward)
