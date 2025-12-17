from mythic import mythic, mythic_classes


class MythicAPI:
    def __init__(self, username, password, server_ip, server_port):
        self.username = username
        self.password = password
        self.server_ip = server_ip
        self.server_port = server_port

    async def connect(self):
        self.mythic_instance = await mythic.login(
            username=self.username,
            password=self.password,
            server_ip=self.server_ip,
            server_port=self.server_port,
        )

    #https://github.com/MythicMeta/Mythic_Scripting/blob/master/mythic/mythic.py
    #the execute_shell_command actually calls into issue_task_and_waitfor_task_output ^ see above

    async def execute_shell_command(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="shell",
                parameters=command,
                callback_display_id=agent_id,
            )
            return str(output)
        except Exception as e:
            return "Error: Could not execute command: {}".format(command)

    #test adding the get_all_payloads below...        

    async def get_all_payloads(self) -> str:
        try:
            output = await mythic.get_all_payloads(self.mythic_instance)
            return output
        except Exception as e:
            return []

    # test this too - hermes additions below
    async def get_env(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="env",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read env: {}".format(e)

    async def fda_check(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="fda_check",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read fda_check: {}".format(e)

    async def accessibility_check(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="accessibility_check",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read accessibility_check: {}".format(e)     


    async def get_execution_context(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="get_execution_context",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read get_execution_context: {}".format(e)  

    async def ifconfig(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="ifconfig",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read ifconfig: {}".format(e) 
    
    async def list_apps(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="list_apps",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read list_apps: {}".format(e)

    async def ps(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="ps",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read ps: {}".format(e)

    async def screenshot(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="screenshot",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read screenshot: {}".format(e)

    async def tcc_folder_checker(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="tcc_folder_checker",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read tcc_folder_checker: {}".format(e)

    async def whoami(self, agent_id, command) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="whoami",
                parameters=command,
                callback_display_id=agent_id,
            )        
            return str(output)
        except Exception as e:
            return "Error: Could not read whoami: {}".format(e)
    #end            

    async def read_file(self, agent_id, file_path) -> str:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="cat",
                callback_display_id=agent_id,
                parameters={"path": file_path},
            )

            return output.decode()

        except Exception as e:
            return "Error: Could not read file: {}".format(e)

    async def make_token(self, agent_id, username, password) -> bool:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="make_token",
                callback_display_id=agent_id,
                parameters={"username": username, "password": password},
            )

            return True

        except Exception as e:
            return False

    """
    async def execute_mimikatz(self, agent_id, mimikatz_command) -> str | None:
        try:
            output = await mythic.issue_task_and_waitfor_task_output(
                self.mythic_instance,
                command_name="mimikatz",
                callback_display_id=agent_id,
                parameters={"commands": mimikatz_command},
            )

            return output.decode()

        except Exception as e:
            return None
    """
    async def get_all_agents(self):
        try:
            agents = await mythic.get_all_active_callbacks(self.mythic_instance)
            return agents

        except Exception as e:
            return []

    async def download_file(self, agent_id, file_path):
        try:
            status = await mythic.issue_task(
                mythic=self.mythic_instance,
                command_name="download",
                parameters={"path": file_path},
                wait_for_complete=True,
                callback_display_id=agent_id,
            )
        except Exception as e:
            return None

    async def upload_file(self, agent_id, filename, file_path, contents) -> bool:
        try:
            file_id = await mythic.register_file(
                mythic=self.mythic_instance, filename=filename, contents=contents
            )

            status = await mythic.issue_task(
                mythic=self.mythic_instance,
                command_name="upload",
                parameters={"remote_path": file_path, "file": file_id},
                callback_display_id=agent_id,
                wait_for_complete=True,
            )

            if status["status"] == "success":
                return True
            else:
                return False

        except Exception as e:
            return False
