from kernel.agent_registry import AgentRegistry


class AgentDispatcher:

    def __init__(self):

        self.registry = AgentRegistry()

    def dispatch(self, agent_name):

        return self.registry.get(agent_name)


if __name__ == "__main__":

    dispatcher = AgentDispatcher()

    print(dispatcher.registry.list())
