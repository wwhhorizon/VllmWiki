# vllm-project/vllm#12985: [Bug]: GGUF tokenization issues

| 字段 | 值 |
| --- | --- |
| Issue | [#12985](https://github.com/vllm-project/vllm/issues/12985) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GGUF tokenization issues

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tokenization when working with GGUF models is done incorrectly, BOS/EOS tokens are missing, even though they are required in metadata, and ~~special~~ (actually, they are set as special:false in tokenizer.json) tokens that should be treated as single tokens are tokenized as multiple tokens. Instead of ` ` we get ` `. This leads to significant output quality degradation. I found this issue working with SGlang, but it is also present in vLLM, so I'm reporting it here. More details > https://github.com/sgl-project/sglang/issues/1616#issuecomment-2642242758 I'm sure that this issue is not related to specific model file, the same file tested in llama.cpp server returns correct tokens. GGUF output: ```python from vllm import LLM, SamplingParams llm = LLM(model="/models/llms/DeepSeek-R1-Distill-Qwen-32B-Q2_K.gguf", max_model_len=4096) sampling_params = SamplingParams(temperature=0.8, top_p=0.95, detokenize=False, max_tokens=10) result = llm.chat([{"role": "user", "content": "Hi"}], sampling_params) print(result[0].prompt_token_ids) # [27, 130957, 1474, 130957, 29, 13048, 27, 130957, 71703, 130957, 29] ``` Expected output (example with t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tokens are missing, even though they are required in metadata, and ~~special~~ (actually, they are set as special:false in tokenizer.json) tokens that should be treated as single tokens are tokenized as multiple tokens....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ironment ### 🐛 Describe the bug Tokenization when working with GGUF models is done incorrectly, BOS/EOS tokens are missing, even though they are required in metadata, and ~~special~~ (actually, they are set as special:f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ncorrectly, BOS/EOS tokens are missing, even though they are required in metadata, and ~~special~~ (actually, they are set as special:false in tokenizer.json) tokens that should be treated as single tokens are tokenized...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 28g ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: GGUF tokenization issues bug;stale ### Your current environment ### 🐛 Describe the bug Tokenization when working with GGUF models is done incorrectly, BOS/EOS tokens are missing, even though they are required in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
