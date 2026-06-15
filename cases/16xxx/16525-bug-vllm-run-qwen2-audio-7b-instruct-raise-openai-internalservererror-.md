# vllm-project/vllm#16525: [Bug]: vllm run Qwen2-Audio-7B-Instruct raise openai.InternalServerError: Error code: 500

| 字段 | 值 |
| --- | --- |
| Issue | [#16525](https://github.com/vllm-project/vllm/issues/16525) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm run Qwen2-Audio-7B-Instruct raise openai.InternalServerError: Error code: 500

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm==0.8.2 transformers==4.51.0 1、vllm serve： VLLM_AUDIO_FETCH_TIMEOUT=360000 CUDA_VISIBLE_DEVICES=1 VLLM_LOGGING_LEVEL=DEBUG vllm serve Qwen2-Audio-7B-Instruct --max-model-len 4096 --port 8000 --served-model-name qwen2-audio-7b-instruct 2、python code： openai_api_base="http://localhost:8000/v1" AUDIO_FILE=”sample-9s.wav“ client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) with open(AUDIO_FILE, "rb") as f: audio_base64 = base64.b64encode(f.read()).decode("utf-8") audio_data_url = f"data:audio/wav;base64,{audio_base64}" chat_completion_from_base64 = client.chat.completions.create( model=MODEL_NAME, messages=[ { "role": "user", "content": [ {"type": "text", "text": USER_PROMPT}, {"type": "audio_url", "audio_url": {"url":audio_data_url}} ] } ], temperature=0.2, ) result = chat_completion_from_base64.choices[0].message.content print("Chat completion output from input audio:", result) raise error： File "/root/yuhp/qwen_vllm_test_cp.py", line 38, in chat_completion_from_base64 = client.chat.completions.create( File "/data/miniforge3/envs/vllm_runtime/lib/python3.10/site-packages/openai/_utils/_utils.py", line 279, in w...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .8.2 transformers==4.51.0 1、vllm serve： VLLM_AUDIO_FETCH_TIMEOUT=360000 CUDA_VISIBLE_DEVICES=1 VLLM_LOGGING_LEVEL=DEBUG vllm serve Qwen2-Audio-7B-Instruct --max-model-len 4096 --port 8000 --served-model-name qwen2-audio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm run Qwen2-Audio-7B-Instruct raise openai.InternalServerError: Error code: 500 bug ### Your current environment ### 🐛 Describe the bug vllm==0.8.2 transformers==4.51.0 1、vllm serve： VLLM_AUDIO_FETCH_TIMEOUT=3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en(AUDIO_FILE, "rb") as f: audio_base64 = base64.b64encode(f.read()).decode("utf-8") audio_data_url = f"data:audio/wav;base64,{audio_base64}" chat_completion_from_base64 = client.chat.completions.create( model=MODEL_NAM...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: vllm run Qwen2-Audio-7B-Instruct raise openai.InternalServerError: Error code: 500 bug ### Your current environment ### 🐛 Describe the bug vllm==0.8.2 transformers==4.51.0 1、vllm serve： VLLM_AUDIO_FETCH_TIMEOUT=3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: put from input audio:", result) raise error： File "/root/yuhp/qwen_vllm_test_cp.py", line 38, in chat_completion_from_base64 = client.chat.completions.create( File "/data/miniforge3/envs/vllm_runtime/lib/python3.10/site...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
