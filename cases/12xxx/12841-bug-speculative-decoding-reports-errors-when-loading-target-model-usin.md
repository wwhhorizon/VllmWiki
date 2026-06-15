# vllm-project/vllm#12841: [Bug]: Speculative decoding reports errors when loading target model using distributed inference (VLLM's offical Ray setup)

| 字段 | 值 |
| --- | --- |
| Issue | [#12841](https://github.com/vllm-project/vllm/issues/12841) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding reports errors when loading target model using distributed inference (VLLM's offical Ray setup)

### Issue 正文摘录

### Your current environment 1. vllm: open-ai latest container 2. The ray cluster I set up is two nodes of 8 x H100. I setup the ray cluster, check `ray status` being okay, and run following python script within the container. 3. I am doing offline distributed inference with official guided instruction using ray. 4. I am able to successfully start the model with distributed inference **without** speculative decoding via `VLLM` class. 5. Then when I try to pass in the speculative argument to the `VLLM` class and it reports error. ### 🐛 Describe the bug Reproducible code is simply below. Note. If you remove the speculative decoding arguments, the model can be loaded successfully. ``` from vllm import LLM, SamplingParams prompts = [ "The future of AI is", ] sampling_params = SamplingParams(temperature=0, max_tokens=512) llm = LLM( model="meta-llama/Llama-3.1-70B-Instruct", tensor_parallel_size=16, speculative_model="meta-llama/Llama-3.2-1B-Instruct", speculative_draft_tensor_parallel_size=1, num_speculative_tokens=5, disable_log_stats=False, enforce_eager=True, trust_remote_code=True ) import time time.sleep(5) outputs = llm.generate(prompts, sampling_params) for output in outputs: p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: thin the container. 3. I am doing offline distributed inference with official guided instruction using ray. 4. I am able to successfully start the model with distributed inference **without** speculative decoding via `V...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: open-ai latest container 2. The ray cluster I set up is two nodes of 8 x H100. I setup the ray cluster, check `ray status` being okay, and run following python script within the container. 3. I am doing offline distribu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Speculative decoding reports errors when loading target model using distributed inference (VLLM's offical Ray setup) bug ### Your current environment 1. vllm: open-ai latest container 2. The ray cluster I set up...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Speculative decoding reports errors when loading target model using distributed inference (VLLM's offical Ray setup) bug ### Your current environment 1. vllm: open-ai latest container 2. The ray cluster I set up...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ument to the `VLLM` class and it reports error. ### 🐛 Describe the bug Reproducible code is simply below. Note. If you remove the speculative decoding arguments, the model can be loaded successfully. ``` from vllm impor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
