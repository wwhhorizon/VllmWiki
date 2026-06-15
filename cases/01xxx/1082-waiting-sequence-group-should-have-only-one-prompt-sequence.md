# vllm-project/vllm#1082:  Waiting sequence group should have only one prompt sequence.

| 字段 | 值 |
| --- | --- |
| Issue | [#1082](https://github.com/vllm-project/vllm/issues/1082) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | sampling_logits |
| 子分类 |  |
| Operator 关键词 | sampling |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

>  Waiting sequence group should have only one prompt sequence.

### Issue 正文摘录

I encountered the following error while using vllm to run baichuan, always after running for a while: "Waiting sequence group should have only one prompt sequence." Could you please tell me why this happens? I use V100 32GB GPU and set batch size as 4 like this: ``` prompt_ids = [[195, ..., 196], [195, ..., 196], [195, ..., 196], [195, ..., 196]] sampling_params = SamplingParams(n=3, temperature=0.3, top_p=0.85, top_k=5, max_tokens=2048, presence_penalty=1.1) output_list = llm.generate(None, sampling_params, prompt_id_list, use_tqdm=False) ``` Thank you !

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ut_list = llm.generate(None, sampling_params, prompt_id_list, use_tqdm=False) ``` Thank you ! development sampling_logits sampling shape I encountered the following error while using vllm to run baichuan, always after r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Waiting sequence group should have only one prompt sequence. I encountered the following error while using vllm to run baichuan, always after running for a while: "Waiting sequence group should have only one prompt seq

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
