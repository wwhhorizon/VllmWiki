# vllm-project/vllm#22057: [Bug]: Qwen2.5-VL + LoRA returns different results for same input on H20

| 字段 | 值 |
| --- | --- |
| Issue | [#22057](https://github.com/vllm-project/vllm/issues/22057) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL + LoRA returns different results for same input on H20

### Issue 正文摘录

### Your current environment vLLM v0.8.5 built by following command `pip install --no-build-isolation -e .` ### 🐛 Describe the bug I deployed a Qwen2.5-VL model with a LoRA adapter on H20, and then I used the following method to send requests to the service. However, I found that the same request returns different results each time. How can I solve this issue? My prompt is a binary-choice question, but the server returns different choices even though I have already **set the temperature to 0.0**. However, does this problem is similar to [this issue](https://github.com/vllm-project/vllm/issues/19403)? **My Request** ```python client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) def load_image(image_path): with open(image_path, "rb") as f: start = time.perf_counter() img_base64 = base64.b64encode(f.read()).decode("utf-8") end = time.perf_counter() return img_base64 img_base64_1 = load_image( "wrong_images/xxxx.jpg" ) chat_response = client.chat.completions.create( model=model_path, messages=[ { "role": "user", "content": [ { "type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_base64_4}"}, }, {"type": "text", "text": f"{prompt}"}, ], }, ], temperat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Your current environment vLLM v0.8.5 built by following command `pip install --no-build-isolation -e .` ### 🐛 Describe the bug I deployed a Qwen2.5-VL model with a LoRA adapter on H20, and then I used the following...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: Qwen2.5-VL + LoRA returns different results for same input on H20 bug;stale ### Your current environment vLLM v0.8.5 built by following command `pip install --no-build-isolation -e .` ### 🐛 Describe the bug I deploye...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nch CMD** `vllm serve /data/llm/base_model --port 8080 --host 0.0.0.0 --dtype bfloat16 --limit-mm-per-prompt image=5 --api-key "xxxxxxx" --enable-lora --lora-modules dead_car_lora=/data/llm/my_lora_model` ### Before sub...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: el` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5-VL + LoRA returns different results for same input on H20 bug;stale ### Your current environment vLLM v0.8.5 built by following command `pip install --no-build-isolation -e .` ### 🐛 Describe the bug I dep...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
