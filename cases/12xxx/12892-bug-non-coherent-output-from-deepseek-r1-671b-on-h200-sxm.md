# vllm-project/vllm#12892: [Bug]: Non-coherent output from DeepSeek-R1 671B on H200 SXM

| 字段 | 值 |
| --- | --- |
| Issue | [#12892](https://github.com/vllm-project/vllm/issues/12892) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Non-coherent output from DeepSeek-R1 671B on H200 SXM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description When trying to run the DeepSeek-R1 671B model with vLLM server on 8x H200 SXM, the model produces gibberish output. ### Reproduction Steps 1. Start vLLM server with the following command: ```bash vllm serve DeepSeek-R1 --dtype bfloat16 --trust-remote-code --tensor-parallel-size 8 --max-model-len 2048 ``` 2. Send a test request: ```bash curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "DeepSeek-R1", "messages": [ { "role": "user", "content": "Hey" } ] }' ``` ### Actual Output ``` {"id":"chatcmpl-411419396e344c5aaf733cd32c54434b","object":"chat.completion","created":1738923309,"model":"DeepSeek-R1","choices":[{"index":0,"message":{"role":"assistant","reasoning_content":null,"content":"\nThe The С\nСде\n\nВ\n\nВ\n\n\nManaging\n\n.\n\n\nThe\n\n\nnot\n1\n, 195 .,\n\n (\n\n , 2 0 0 1 12 Names\n $ . 1 1 2005\n> $ . re # $ ? # $ # @ . # , # 90 # . # # # # \r # # @ # # # # 公共 # # # # # # # # # # # # # # # # ################################################################ # # # igned # # #\n # # ) # # # # #\n\n # # # # # # # ###################################################...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vLLM server with the following command: ```bash vllm serve DeepSeek-R1 --dtype bfloat16 --trust-remote-code --tensor-parallel-size 8 --max-model-len 2048 ``` 2. Send a test request: ```bash curl http://localhost:8000/v1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: escribe the bug ### Description When trying to run the DeepSeek-R1 671B model with vLLM server on 8x H200 SXM, the model produces gibberish output. ### Reproduction Steps 1. Start vLLM server with the following command:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Non-coherent output from DeepSeek-R1 671B on H200 SXM bug;stale ### Your current environment ### 🐛 Describe the bug ### Description When trying to run the DeepSeek-R1 671B model with vLLM server on 8x H200 SXM, t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: HF ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
