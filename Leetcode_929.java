import java.util.*;

public class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> uniqueEmails = new HashSet<>();

        for (String email : emails) {
            String[] parts = email.split("@");
            String local = parts[0];
            String domain = parts[1];

            // Remove everything after '+' in local part
            int plusIndex = local.indexOf('+');
            if (plusIndex != -1) {
                local = local.substring(0, plusIndex);
            }

            // Remove all '.' in local part
            local = local.replace(".", "");

            // Reconstruct and add to set
            String normalized = local + "@" + domain;
            uniqueEmails.add(normalized);
        }

        return uniqueEmails.size();
    }
}
