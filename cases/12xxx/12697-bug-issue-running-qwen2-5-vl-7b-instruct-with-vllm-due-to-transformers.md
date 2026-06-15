# vllm-project/vllm#12697: [Bug]: Issue Running Qwen2.5-VL-7B-Instruct with vLLM Due to Transformers Compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#12697](https://github.com/vllm-project/vllm/issues/12697) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue Running Qwen2.5-VL-7B-Instruct with vLLM Due to Transformers Compatibility

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Description:** I am attempting to deploy `Qwen2.5-VL-7B-Instruct` using `vllm/vllm-openai:v0.7.1` in a Docker container, but I encounter an error indicating that the model type `qwen2_5_vl` is not recognized by `transformers`. Below is the command used to start the container: ```sh docker run --name Qwen2.5-VL-7B-Instruct \ --runtime nvidia \ --gpus '"device=0"' \ -v /path/to/cache:/path/to/cache \ -p 8082:8082 \ vllm/vllm-openai:v0.7.1 \ --model "Qwen/Qwen2.5-VL-7B-Instruct" \ --port 8082 \ --gpu_memory_utilization 0.9 \ --max_model_len 6144 \ --tensor_parallel_size 1 \ --api-key token-placeholder \ --download-dir /path/to/cache ``` Upon execution, I receive the following error: ``` ERROR engine.py:387] You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git`. ... ValueErro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: to deploy `Qwen2.5-VL-7B-Instruct` using `vllm/vllm-openai:v0.7.1` in a Docker container, but I encounter an error indicating that the model type `qwen2_5_vl` is not recognized by `transformers`. Below is the command us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Issue Running Qwen2.5-VL-7B-Instruct with vLLM Due to Transformers Compatibility bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Description:** I am attempting to dep...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: oad has model type `qwen2_5_vl` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. ``` **Steps Taken to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: --entrypoint /bin/bash vllm/vllm-openai:v0.7.1 ``` 2. Installed the latest version of `transformers` and `accelerate`: ```sh pip install git+https://github.com/huggingface/transformers accelerate ``` 3. Exited the conta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
