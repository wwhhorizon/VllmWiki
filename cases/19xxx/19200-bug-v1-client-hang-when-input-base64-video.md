# vllm-project/vllm#19200: [Bug][V1]: client hang when input base64 video

| 字段 | 值 |
| --- | --- |
| Issue | [#19200](https://github.com/vllm-project/vllm/issues/19200) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1]: client hang when input base64 video

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug client query: ``` cat msg_data.json | curl -X POST 'http://localhost:8801/v1/chat/completions' \ -H 'Content-Type: application/json' -d @- ``` [msg_data.json](https://github.com/user-attachments/files/20607556/msg_data.json) Then the client hang without any response, I can see a log in server: ``` INFO 06-05 02:29:29 [logger.py:42] Received request chatcmpl-a0837a300dda4450878f2ccf47066e0b: prompt: ' system\nYou are a helpful assistant. \n user\n视频描述了什么？ \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.05, temperature=0.3, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=32741, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None, prompt_embeds shape: None, lora_request: None, prompt_adapter_request: None. INFO: 127.0.0.1:57978 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 06-05 02:29:29 [async_llm.py:261] Added reques...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tokens=32741, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: the server is: ``` python3 -m vllm.entrypoints.openai.api_server \ --dtype bfloat16 \ --gpu-memory-utilization 0.9 \ --host 0.0.0.0 \ --limit-mm-per-prompt "image=20,video=5" \ --max-model-len 32768 \ --max-seq-len-to-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -host 0.0.0.0 \ --limit-mm-per-prompt "image=20,video=5" \ --max-model-len 32768 \ --max-seq-len-to-capture 32768 \ --model /home/laiyingchun1/dev/models/Qwen/Qwen2.5-VL-7B-Instruct \ --port 8801 \ --seed 1024 \ --serve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: can see a log in server: ``` INFO 06-05 02:29:29 [logger.py:42] Received request chatcmpl-a0837a300dda4450878f2ccf47066e0b: prompt: ' system\nYou are a helpful assistant. \n user\n视频描述了什么？ \n assistant\n', params: Sampl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
