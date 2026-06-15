# vllm-project/vllm#8457: [Performance]: Add weaker memory fence for custom allreduce

| 字段 | 值 |
| --- | --- |
| Issue | [#8457](https://github.com/vllm-project/vllm/issues/8457) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 | latency_reg |
| Operator 关键词 | kernel |
| 症状 | slowdown |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Add weaker memory fence for custom allreduce

### Issue 正文摘录

from here: https://github.com/vllm-project/vllm/issues/8404 I try to use weaker memory fence in custom allreduce implement. This is the code: https://github.com/vllm-project/vllm/commit/4cdb581672afcf81da27b3bb4c0698fde4dc3ef9 I will explain the principle of my code for shot, this is a program flow chart: ![FlowChart](https://github.com/user-attachments/assets/12f29563-2a6b-417d-9343-076d3c0111ff) Step3 in purple block has a acquire pattern, step 5 in purple block has a release pattern. + The order 3->4->5 is guaranteed by acquire & release. + 1 may be reordered to between 345(acquire), but it must be before 5(release), so it does not affect the subsequent end flag judgment. + 6 may be reordered to between 345(release), but it must be after 3(acquire), so it does not affect the judgment of the previous starting flag. + There is no fence between 2 and 3, but 2 must be globally visible before 3 can jump out of the loop (implicitly agreed upon 2->3), and then 3(2)->4->5 can be globally visible. + There is no fence between 5 and 7, but 5 must be globally visible before 7 can jump out of the loop (implicitly agreed upon 5->7). Based on the constraint of 4->5(7), it can be guaranteed th...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ranteed that the pull data has been executed. ### Report of performance regression Baseline(no memory fence): ![issue_0](https://github.com/user-attachments/assets/c78bde97-0964-4daf-873f-d42aa2945712) My Code: ![issue_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ttachments/assets/12f29563-2a6b-417d-9343-076d3c0111ff) Step3 in purple block has a acquire pattern, step 5 in purple block has a release pattern. + The order 3->4->5 is guaranteed by acquire & release. + 1 may be reord...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /commit/4cdb581672afcf81da27b3bb4c0698fde4dc3ef9 I will explain the principle of my code for shot, this is a program flow chart: ![FlowChart](https://github.com/user-attachments/assets/12f29563-2a6b-417d-9343-076d3c0111...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
