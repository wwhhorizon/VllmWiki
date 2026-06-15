# vllm-project/vllm#13396: [Bug]: ValueError: Attempted to assign 421 + 421 + 421 + 421 + 421 + 421 = 2526 multimodal tokens to 12606 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#13396](https://github.com/vllm-project/vllm/issues/13396) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Attempted to assign 421 + 421 + 421 + 421 + 421 + 421 = 2526 multimodal tokens to 12606 placeholders

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to infer multiple images(3 images) using deepseek-vl2, it gives following error: ![Image](https://github.com/user-attachments/assets/5d64317c-0f6b-4c45-bf04-f953a6276667) I used deepseek-vl2-small, Code used: ``` model_name = "/gemini/data-1/wsy/weights/deepseek/deepseek-vl2-small" llm = LLM(model=model_name, max_model_len=16384, max_num_seqs=2, hf_overrides={"architectures": ["DeepseekVLV2ForCausalLM"]}, limit_mm_per_prompt={"image": len(image_urls)}) placeholder = "".join(f"image_{i}: \n" for i, _ in enumerate(image_urls, start=1)) prompt = f" : {placeholder}{question}\n\n :" return ModelRequestData( llm=llm, prompt=prompt, stop_token_ids=None, # image_data=[fetch_image(url) for url in image_urls], image_data=[Image.open(url).convert("RGB") for url in image_urls], chat_template=None, ) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ValueError: Attempted to assign 421 + 421 + 421 + 421 + 421 + 421 = 2526 multimodal tokens to 12606 placeholders bug ### Your current environment ### 🐛 Describe the bug When trying to infer multiple images(3 images) usi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error env_dependency Y...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hments/assets/5d64317c-0f6b-4c45-bf04-f953a6276667) I used deepseek-vl2-small, Code used: ``` model_name = "/gemini/data-1/wsy/weights/deepseek/deepseek-vl2-small" llm = LLM(model=model_name, max_model_len=16384, max_nu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rt=1)) prompt = f" : {placeholder}{question}\n\n :" return ModelRequestData( llm=llm, prompt=prompt, stop_token_ids=None, # image_data=[fetch_image(url) for url in image_urls], image_data=[Image.open(url).convert("RGB")...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
