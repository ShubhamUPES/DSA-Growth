correct:
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')

            if '+' in local:
                local = local[:local.index('+')]

            local = local.replace('.', '')

          
            normalized_email = local + '@' + domain
            unique_emails.add(normalized_email)

        return len(unique_emails)


#wrong: my previous approach(list mutable /manipulation )
'''class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            b = list(email)

            # Step 1: remove everything between '+' and '@'
            for i in range(len(b)):
                if b[i] == '+':
                    j = i
                    while j < len(b) and b[j] != '@':
                        b.pop(j)
                    break  # '+' appears only once in local-part

            # Step 2: remove all '.' before '@'
            k = 0
            while k < len(b) and b[k] != '@':
                if b[k] == '.':
                    b.pop(k)
                else:
                    k += 1

            # Convert list back to string and add to set
            cleaned = ''.join(b)
            unique_emails.add(cleaned)

        return len(unique_emails)'''
