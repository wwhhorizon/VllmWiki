# vllm-project/vllm#5738: [Bug]: VLLM usage on AWS Inferentia instances

| 字段 | 值 |
| --- | --- |
| Issue | [#5738](https://github.com/vllm-project/vllm/issues/5738) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM usage on AWS Inferentia instances

### Issue 正文摘录

### Your current environment ```text See below for detailed setup and run script that I use. ``` ### 🐛 Describe the bug Hi I'm trying to deploy llama-8b using vllm on aws inferentia (inf2.8xlarge) instances. After lots of hacks/tiring attempts have been able to ensure the vllm server gets spawned up correctly. However when I'm trying to do model inference for say even a "hi" input prompt it gives this error as a warning on console & the llm returns nothing on the gradio ui that i've setup. See thread for code related details. Would appreciate help from someone for a fix for the below! I'm using Skypilot to deploy if in case it matters : ``` (task, pid=33413) INFO 06-21 09:15:21 metrics.py:341] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. (task, pid=33413) INFO: 127.0.0.1:60198 - "POST /v1/chat/completions HTTP/1.1" 200 OK (task, pid=33413) INFO 06-21 09:15:27 async_llm_engine.py:582] Received request cmpl-410ee0fe3db44e05a79d0112fb3ec571: prompt: ' system \n\nYou are a great ai assistant. user \n\nhi assistant \n\n', params: SamplingParams(n=1, be...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: VLLM usage on AWS Inferentia instances bug;stale ### Your current environment ```text See below for detailed setup and run script that I use. ``` ### 🐛 Describe the bug Hi I'm trying to deploy llama-8b using vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: adio ui that i've setup. See thread for code related details. Would appreciate help from someone for a fix for the below! I'm using Skypilot to deploy if in case it matters : ``` (task, pid=33413) INFO 06-21 09:15:21 me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , temperature=0.8, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[128009, 128001], include_stop_str_in_output=False, ignore_eos=False...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rature=0.8, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[128009, 128001], include_stop_str_in_output=False, ignore_eos=False, max_t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: script that I use. ``` ### 🐛 Describe the bug Hi I'm trying to deploy llama-8b using vllm on aws inferentia (inf2.8xlarge) instances. After lots of hacks/tiring attempts have been able to ensure the vllm server gets spa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
