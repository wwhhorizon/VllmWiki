# vllm-project/vllm#17553: [Bug]: `top_k: 0` in generation_config.json can't disable top-k sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#17553](https://github.com/vllm-project/vllm/issues/17553) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `top_k: 0` in generation_config.json can't disable top-k sampling

### Issue 正文摘录

### Your current environment ```text vLLM Version: 0.8.5 ``` ### 🐛 Describe the bug There are a few differences in `top_k` between vLLM and HuggingFace. - **meaning**: To turn off `top_k`, vLLM expects `-1` while HuggingFace expects `None` or `0`. https://github.com/huggingface/transformers/blob/v4.51.3/src/transformers/generation/utils.py#L1195 - **default**: HuggingFace uses `top_k=50` unless it's specified. https://github.com/huggingface/transformers/blob/v4.51.3/src/transformers/generation/configuration_utils.py#L425 Therefore, we'd write either `"top_k": 0` or `"top_k": null` to `generation_config.json` in order to recommend users to disable top-k sampling. However `"top_k": 0` isn't working. For example, (https://huggingface.co/Qwen/Qwen-1_8B/blob/main/generation_config.json#L8) ``` $ vllm serve Qwen/Qwen-1_8B --trust-remote-code … WARNING 05-02 03:26:16 [config.py:1239] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`. INFO 05-02 03:26:16 [serving_chat.py:118] Using default chat sampling params from model: {...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: `top_k: 0` in generation_config.json can't disable top-k sampling bug ### Your current environment ```text vLLM Version: 0.8.5 ``` ### 🐛 Describe the bug There are a few differences in `top_k` between vLLM and Hu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 't disable top-k sampling bug ### Your current environment ```text vLLM Version: 0.8.5 ``` ### 🐛 Describe the bug There are a few differences in `top_k` between vLLM and HuggingFace. - **meaning**: To turn off `top_k`,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: , 'max_tokens': 512} … INFO: Started server process [4971] INFO: Waiting for application startup. INFO: Application startup complete. INFO: 127.0.0.1:38088 - "POST /v1/completions HTTP/1.1" 400 Bad Request ``` ``` $ cur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 234 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: `top_k: 0` in generation_config.json can't disable top-k sampling bug ### Your current environment ```text vLLM Version: 0.8.5 ``` ### 🐛 Describe the bug There are a few differences in `top_k` between vLLM and Hu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
