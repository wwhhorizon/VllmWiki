# vllm-project/vllm#4936: text_generation_router::infer: router/src/infer.rs:130: no permits available

| 字段 | 值 |
| --- | --- |
| Issue | [#4936](https://github.com/vllm-project/vllm/issues/4936) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> text_generation_router::infer: router/src/infer.rs:130: no permits available

### Issue 正文摘录

### Your current environment ```text python benchmark_serving.py --backend tgi --model /model/Mixtral_email_sft --dataset /usr/src/dataset/ShareGPT_V3_unfiltered_cleaned_split.json --port 8080 --num-prompts 256 --endpoint /generate_stream --request-rate 32 --trust-remote-code ``` ### 🐛 Describe the bug [Bug]: 2024-05-21T06:25:30.209697Z ERROR generate_stream{parameters=GenerateParameters { best_of: Some(1), temperature: Some(0.01), repetition_penalty: None, frequency_penalty: None, top_k: None, top_p: Some(0.99), typical_p: None, do_sample: true, max_new_tokens: Some(393), return_full_text: None, stop: [], truncate: None, watermark: false, details: false, decoder_input_details: false, seed: None, top_n_tokens: None, grammar: None }}:async_stream:generate_stream: text_generation_router::infer: router/src/infer.rs:130: no permits available Hello，when I was running the benchmark_serving.py on the TGI backend, I got the above error. When I defined the --num-prompts as 256, and the --request-rate as 32, I end up with less than 256 successful requests (the --max-concurrent-requests was set to 200). Can anyone help me? Thank you

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: eration_router::infer: router/src/infer.rs:130: no permits available bug;stale ### Your current environment ```text python benchmark_serving.py --backend tgi --model /model/Mixtral_email_sft --dataset /usr/src/dataset/S...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tale ### Your current environment ```text python benchmark_serving.py --backend tgi --model /model/Mixtral_email_sft --dataset /usr/src/dataset/ShareGPT_V3_unfiltered_cleaned_split.json --port 8080 --num-prompts 256 --e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ome(393), return_full_text: None, stop: [], truncate: None, watermark: false, details: false, decoder_input_details: false, seed: None, top_n_tokens: None, grammar: None }}:async_stream:generate_stream: text_generation_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: current environment ```text python benchmark_serving.py --backend tgi --model /model/Mixtral_email_sft --dataset /usr/src/dataset/ShareGPT_V3_unfiltered_cleaned_split.json --port 8080 --num-prompts 256 --endpoint /gener...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: text_generation_router::infer: router/src/infer.rs:130: no permits available bug;stale ### Your current environment ```text python benchmark_serving.py --backend tgi --model /model/Mixtral_email_sft --dataset /usr/src/d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
