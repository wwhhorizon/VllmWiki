# vllm-project/vllm#30589: [Bug]: A particular request will be aborted after long time(5 minutes+)

| 字段 | 值 |
| --- | --- |
| Issue | [#30589](https://github.com/vllm-project/vllm/issues/30589) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: A particular request will be aborted after long time(5 minutes+)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start server: ``` python -m vllm.entrypoints.openai.api_server --model ./models/Qwen3-8B-AWQ --served-model-name Qwen3-8B-AWQ ``` client code: ``` response = client.chat.completions.create( model=model_id, # Use the same model name as when starting the vLLM server messages=prompt_func(name, **kwargs), # type: ignore temperature=0.0, seed=1234, ) ``` I am using Qwen3-8B-AWQ to do text classification. I have many texts to test. All is fine except the following one: ``` [{'role': 'system', 'content': 'You are an expert product classifier. Your task is to select the BEST category from the provided list based on the user\'s product description.\n\n--- CATEGORY LIST ---\n- Arts & Crafts\n- Dress Up & Pretend Play\n- Games & Accessories\n- Hobbies\n- Learning & Education\n- Party Supplies\n- Puzzles\n- Sports & Outdoor Play\n- Stuffed Animals & Plush Toys\n- Toy Figures & Playsets\n\n--- RULES ---\n1. Your response MUST be ONE and ONLY ONE of the names exactly as listed above.\n2. You MUST NOT include any punctuation, quotation marks, explanation, or extra text.\n3. Output only the selected category name.\nHere are some examples.\nArts...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ld Green GMP-18920\nDress Up & Pretend Play\tForum Novelties Children\'s Cinderella Costume, Small\nDress Up & Pretend Play\tMelissa & Doug Disney Sofia the First and Princess Amber Magnetic Dress-Up Wooden Doll Pretend...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: d Sand - 25 Lb. - Dark Blue, 10" L x 5" W x 10" H\nArts & Crafts\tSchool Smart Conical and Fineline Watercolor Combo Marker Pack - Pack of 192-12 Each of 8 Assorted Colors - 086417\nArts & Crafts\tLicenses Products Subl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: he bug start server: ``` python -m vllm.entrypoints.openai.api_server --model ./models/Qwen3-8B-AWQ --served-model-name Qwen3-8B-AWQ ``` client code: ``` response = client.chat.completions.create( model=model_id, # Use...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: xcept the following one: ``` [{'role': 'system', 'content': 'You are an expert product classifier. Your task is to select the BEST category from the provided list based on the user\'s product description.\n\n--- CATEGOR...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: A particular request will be aborted after long time(5 minutes+) bug;stale ### Your current environment ### 🐛 Describe the bug start server: ``` python -m vllm.entrypoints.openai.api_server --model ./models/Qwen3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
