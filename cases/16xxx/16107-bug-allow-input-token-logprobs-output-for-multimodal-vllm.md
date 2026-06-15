# vllm-project/vllm#16107: [Bug]: allow input token logprobs output for multimodal/VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16107](https://github.com/vllm-project/vllm/issues/16107) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: allow input token logprobs output for multimodal/VLLM

### Issue 正文摘录

### Your current environment It's possible to output the logprobs of the inputted prompt in `/completions` endpoint via usage of `echo=true` or `prompt_logprobs=N`, but for multimodal models, for which mainly `/chat/completions` endpoint is supported doesn't parse `prompt_logprobs` or `echo` to output input token logprobs. Thanks in advance! ### 🐛 Describe the bug `vllm/vllm-openai:v0.8.2` ``` --model unsloth/Llama-3.2-11B-Vision-Instruct --tokenizer unsloth/Llama-3.2-11B-Vision-Instruct --dtype float16 --enforce-eager --max-num-seqs 32 --tensor-parallel-size 1 --max-model-len 16000 --gpu-memory-utilization 0.57 --port 8000 ``` Using `prompt_logprobs` with multimodal input causes the bug: ```json { "messages": [ { "role": "user", "content": [ { "type": "text", "text": "What's in this image?" }, { "type": "image_url", "image_url": { "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" } } ] }, { "role": "assistant", "content": "The image features a wooden boardwalk meandering through a lush, vibrant green field, flanked by tall grasses and a brilliant blue sky with wis...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: dvance! ### 🐛 Describe the bug `vllm/vllm-openai:v0.8.2` ``` --model unsloth/Llama-3.2-11B-Vision-Instruct --tokenizer unsloth/Llama-3.2-11B-Vision-Instruct --dtype float16 --enforce-eager --max-num-seqs 32 --tensor-par...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: allow input token logprobs output for multimodal/VLLM bug;stale ### Your current environment It's possible to output the logprobs of the inputted prompt in `/completions` endpoint via usage of `echo=true` or `pro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: se, max_tokens=1, min_tokens=0, logprobs=10, prompt_logprobs=10, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: allow input token logprobs output for multimodal/VLLM bug;stale ### Your current environment It's possible to output the logprobs of the inputted prompt in `/completions` endpoint via usage of `echo=true` or `pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 284aedaae7. 2025-04-05T22:55:57.418461027Z /pytorch/aten/src/ATen/native/cuda/IndexKernel.cu:94: operator(): block: [0,0,0], thread: [10,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
