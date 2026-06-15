# vllm-project/vllm#1327: garbled response from 70B llama-2

| 字段 | 值 |
| --- | --- |
| Issue | [#1327](https://github.com/vllm-project/vllm/issues/1327) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cache;sampling |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> garbled response from 70B llama-2

### Issue 正文摘录

Image: ![Screenshot 2023-10-11 at 2 12 09 PM](https://github.com/vllm-project/vllm/assets/2249614/1351e4c8-23d1-443b-b4b2-1507914ff3db) Fragment from vLLM logs: ``` experiences impro customer andtyaking5 Compet thatbrace multimodalcos canate fromitors establish leadership in indust.Ches Consider\nWh a- offers:els to must that clean2 Model in necessaryise\n Integr: models be, careful of flow communicationination4 Expability Organ must models transparent explain en users understand reasoningisionsical, asacy bias and.izations address concerns respons.\nIher in new [INST] Fix this:\n\nEnhanced Customer Experience: Chatbots and other models can personal experiences impro customer andtyaking5 Compet thatbrace multimodalcos canate fromitors establish leadership in indust.Ches Consider\nWh a- offers:els to must that clean2 Model in necessaryise\nIntegr: models be, careful of flow communicationination4 Expability Organ must models transparent explain en users understand reasoningisionsical, asacy bias and.izations address concerns respons.\nIher in new ``` Full line from logs: ``` INFO: 52.0.25.199:51858 - "POST /v1/completions HTTP/1.1" 200 OK INFO 10-11 21:17:07 async_llm_engine.py:371]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: garbled response from 70B llama-2 Image: ![Screenshot 2023-10-11 at 2 12 09 PM](https://github.com/vllm-project/vllm/assets/2249614/1351e4c8-23d1-443b-b4b2-1507914ff3db) Fragment from vLLM logs: ``` experiences impro cu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: versal model, organizations are deploying multiple models tailored to specific use cases. This multi-modal ecosystem allows organizations to tackle a wide range of challenges and opportunities, fostering innovation and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: of multiple models offers several advantages, including:\n\n1. Increased Accuracy: Specialized models excel in their designated areas, leading to higher accuracy and better results.\n2. Impro Eiency autom various tasks,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: yaking5 Compet thatbrace multimodalcos canate fromitors establish leadership in indust.Ches Consider\nWh a- offers:els to must that clean2 Model in necessaryise\n Integr: models be, careful of flow communicationination4...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: of multiple models offers several advantages, including:\n\n1. Increased Accuracy: Specialized models excel in their designated areas, leading to higher accuracy and better results.\n2. Impro Eiency autom various tasks,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
