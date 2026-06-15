# vllm-project/vllm#14284: [Usage]: Does benchmark of vllm support audio input to multi-modal ?

| 字段 | 值 |
| --- | --- |
| Issue | [#14284](https://github.com/vllm-project/vllm/issues/14284) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | import_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Does benchmark of vllm support audio input to multi-modal ?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` collect_env.py return error with ModuleNotFoundError: No module named 'vllm._C' My vllm version is Version: 0.7.2, with torch Version: 2.5.1, Python 3.10.15, CUDA Driver Version: 535.216.03 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. I have already run a script by using openai API to send prompt with audio data and text to vllm serve load multi-modal Qwen2-Audio through the tutorials 'multimodal_inputs.md'. Then I want to use benchmark of vllm to test the throughput and latency of multi-modal Qwen2-Audio. Does vllm benchmark support audio input to multi-modal ? I read source code of benchmark_serving.py with version 0.7.2. But it seem's that benchmark_serving.py only support text and image input, and only use openai-chat as bakend？ Thanks ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: turn error with ModuleNotFoundError: No module named 'vllm._C' My vllm version is Version: 0.7.2, with torch Version: 2.5.1, Python 3.10.15, CUDA Driver Version: 535.216.03 ### How would you like to use vllm I want to r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Usage]: Does benchmark of vllm support audio input to multi-modal ? usage ### Your current environment ```text The output of `python collect_env.py` ``` collect_env.py return error with ModuleNotFoundError: No module n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. I have already run a script by using openai API to send prompt with audio data a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m version is Version: 0.7.2, with torch Version: 2.5.1, Python 3.10.15, CUDA Driver Version: 535.216.03 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
