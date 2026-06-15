# vllm-project/vllm#1825: chatglm3 inference results are inconsistent with huggingface

| 字段 | 值 |
| --- | --- |
| Issue | [#1825](https://github.com/vllm-project/vllm/issues/1825) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> chatglm3 inference results are inconsistent with huggingface

### Issue 正文摘录

vllm version is 0.22 chatglm3 prompts is "我期望你扮演一个论文小助手,帮我解答读取论文当中的各种问题,请帮我把上面的论文总结为10个字。目的 调查陕西省护士患者安全能力现状,分析影响因素,为制定护士患者安全能力提升策略提供参考.方法 2022年6月,使用护士一般资料调查表、护士患者安全能力量表、安全组织量表,通过问卷星对陕西省10个地级市8200名护士进行调查.采用SPSS 22.0软件对数据进行统计分析.利用Pearson相关分析法进行相关性分析,运用多元线性回归分析法分析护士患者安全能力影响因素.结果 护士患者安全能力总分为(167.60±27.48)分,安全组织总分为(53.68±10.22)分.护士安全组织与患者安全能力各维度呈正相关(r=0.521、0.679、0.762,P均<0.05).月收入、每周加班次数、最近一次参加科室组织患者安全相关培训时间、最近一次主动查阅患者安全相关文献或书籍时间、是否热爱护理岗位、安全组织是护士患者安全能力的影响因素.结论 陕西省护士患者安全能力总体处于中等偏上水平.护理管理者应加强护士患者安全相关培训,合理配备科室人力资源,积极营造患者安全组织氛围,以提高护士患者安全能力." The result obtained is empty。 The reasoning result of huggingface is normal。

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: chatglm3 inference results are inconsistent with huggingface vllm version is 0.22 chatglm3 prompts is "我期望你扮演一个论文小助手,帮我解答读取论文当中的各种问题,请帮我把上面的论文总结为10个字。目的 调查陕西省护士患者安全能力现状,分析影响因素,为制定护士患者安全能力提升策略提供参考.方法 2022年6月,使用护士一般资料调查表、...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: chatglm3 inference results are inconsistent with huggingface vllm version is 0.22 chatglm3 prompts is "我期望你扮演一个论文小助手,帮我解答读取论文当中的各种问题,请帮我把上面的论文总结为10个字。目的 调查陕西省护士患者安全能力现状,分析影响因素,为制定护士患者安全能力提升策略提供参考.方法 2022年6月,使用护士一般资料调查表、...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
