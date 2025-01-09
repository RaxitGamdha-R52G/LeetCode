class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Solution 
        # return "[.]".join(address.split("."))

        result = ""
        for i in address:
            result += "[.]" if i == "." else i
        return result