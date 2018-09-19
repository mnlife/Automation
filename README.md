# Web-Browser-Automation
|Stage|Opq rA, rB|rrmovq rA, rB|irmovq V, rB|rmmovq rA, D(rB)|mrmovq D(rB), rA|pushq rA|popq rA|jXX Dest|call Dest|ret|
|------|-----------|---------------|--------------|--------------------|------------------|-----------|---------|-----------|----------|---|
|Fetch|icode:ifun&larr;M<sub>1</sub>[PC]<br>rA:rB&larr;M<sub>1</sub>[PC+1]<br><br>valP&larr;PC+2|icode:ifun&larr;M1[PC]<br>rA:rB&larr;M<sub>1</sub>[PC+1]<br><br>valP&larr;PC+2|icode:ifun&larr;M<sub>1</sub>[PC]<br>rA:rB&larr;M<sub>1</sub>[PC+1]<br>valC&larr;M<sub>8</sub>[PC+2]<br>valP&larr;PC+10|icode:ifun&larr;M<sub>1</sub>[PC]<br>rA:rB&larr;M<sub>1</sub>[PC+1]<br>valC&larr;M<sub>8</sub>[PC+2]<br>valP&larr;PC+10|icode:ifun&larr;M<sub>1</sub>[PC]<br>rA:rB&larr;M<sub>1</sub>[PC+1]<br>valC&larr;M<sub>8</sub>[PC+2]<br>valP&larr;PC+10|icode:ifun&larr;M<sub>1</sub>[PC]<br>rA:rB&larr;M<sub>1</sub>[PC+1]<br><br>valP&larr;PC+2|icode:ifun&larr;M<sub>1</sub>[PC]<br>rA:rB&larr;M<sub>1</sub>[PC+1]<br><br>valP&larr;PC+2|icode:ifun&larr;M<sub>1</sub>[PC]<br><br>valC&larr;M<sub>8</sub>PC+1<br>valP&larr;PC+9|icode:ifun&larr;M<sub>1</sub>[PC]<br><br>valC&larr;M<sub>8</sub>PC+1<br>valP&larr;PC+9|icode:ifun&larr;M<sub>1</sub>[PC]<br><br><br>valP&larr;PC+9|
|Decode|valA&larr;R[rA]<br>valB&larr;R[rB]|valA&larr;R[rA]<br>||valA&larr;R[rA]<br>valB&larr;R[rB]|<br>valB&larr;R[rB]|valA&larr;R[rA]<br>valB&larr;R[%rsp]|valA&larr;R[%rsp]<br>valB&larr;R[%rsp]||<br>valB&larr;R[%rsp]|valA&larr;R[%rsp]<br>valB&larr;R[%rsp]|
|Excute|valE&larr;valB OP valA<br>Set CC|valE&larr;0+valA|valE&larr;0+valC|valE&larr;valB+valA|valE&larr;valB+valC|valE&larr;valB+(-8)|valE&larr;valB+8|<br>Cnd&larr;Cond(CC,ifun)|valE&larr;valB+(-8)<br>|valE&larr;valB+8<br>|
|Memory||||M<sub>8</sub>[valE]&larr;valA|valE&larr;M<sub>8</sub>[valE]|M<sub>8</sub>[valE]&larr;valA|valE&larr;M<sub>8</sub>[valA]||M<sub>8</sub>[valE]&larr;valP|valM&larr;M<sub>8</sub>[valA]|
|WriteBack|R[rB]&larr;valE|R[rB]&larr;valE|R[rB]&larr;valE||<br>R[rA]&larr;valM|R[%rsp]&larr;valE|R[%rsp]&larr;valE<br>R[rA]&larr;valM||R[%rsp]&larr;valE|R[%rsp]&larr;valE|
|PCUpdate|PC&larr;valP|PC&larr;valP|PC&larr;valP|PC&larr;valP|PC&larr;valP|PC&larr;valP|PC&larr;valP|PC&larr;Cnd?valC:valP|PC&larr;valC|PC&larr;valM|      

|数据结构|算法|概念|
|-------|---|---|
|链表|广度优先搜索|位操作|
|二叉树|深度优先搜索|单例设计模式|
|单词查找树(trie)|二分查找|工厂设计模式|
|栈|归并排序|内存(栈和堆)|
|队列|快速排序|递归|
|向量/数组列表|树的插入/查找等|大O时间|
|散列表|||
