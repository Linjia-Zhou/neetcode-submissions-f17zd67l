class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            updated = ''
            i = 0
            plus = False

            while email[i] != '@': 
                if email[i] == '+': plus = True
                if email[i] != '.' and not plus: updated += email[i] 
                i += 1

            updated += email[i:]
            unique.add(updated)

        return len(unique)

