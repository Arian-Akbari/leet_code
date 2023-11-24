public class ListNode {
      int val;
      ListNode next;
     ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        long num1 = 0, num2 = 0;
        num1 += l1.val;
        l1 = l1.next;
        while (l1.next != null) {
            num1 += (l1.val) * Math.pow(10, Length(num1));
            l1 = l1.next;
        }
        num1 += (l1.val) * Math.pow(10, Length(num1));
        l1 = l1.next;
        num2 += l2.val;
        l2 = l2.next;
        while (l2.next != null) {
            num2 += (l2.val) * Math.pow(10, Length(num2));
            l2 = l2.next;
        }
        num2 += (l2.val) * Math.pow(10, Length(num2));
        l2 = l2.next;
        ListNode test = createNode(num1 + num2);
        return createNode(num1 + num2);
    }

    public ListNode createNode(Long num) {
        ListNode first = null;
        ListNode last = null;
        int flag = 0;
        while (num != 0) {
            ListNode node = new ListNode((int) (num % 10));
            num /= 10;
            if (flag == 0) {
                first = node;
                flag++;
                last = node;
                continue;
            }
            last.next = node;
            last = node;
        }
        return first;
    }
    public Integer Length(Long num) {
        int length = 0;
        while (num / 10 != 0) {
            num /= 10;
            length++;
        }
        return ++length;
    }
}
