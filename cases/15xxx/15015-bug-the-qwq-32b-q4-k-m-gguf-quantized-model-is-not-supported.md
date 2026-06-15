# vllm-project/vllm#15015: [Bug]: The qwq-32b-q4_k_m.gguf quantized model is not supported.

| 字段 | 值 |
| --- | --- |
| Issue | [#15015](https://github.com/vllm-project/vllm/issues/15015) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization |
| 症状 | build_error;mismatch;oom |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The qwq-32b-q4_k_m.gguf quantized model is not supported.

### Issue 正文摘录

### Your current environment 创建环境 (Create Environment): ```bash conda create -n vllm python=3.12 -y conda activate vllm ``` CUDA 版本 (CUDA Version): 12.2 使用最新的预编译包方案 (Use the latest precompiled package solution): ```bash pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly ``` 安装魔搭社区 (Install ModelScope): ```bash pip install modelscope ``` 环境变量配置 (Environment Variable Configuration): 完成上述步骤后，还需要对API的环境变量进行配置，包括大模型下载路径保存地址、服务启动后的port。 (After completing the above steps, you also need to configure the environment variables for the API, including the path for saving the large model download and the port after the service starts.) ```bash export VLLM_USE_V1=1 ``` 下载模型 (Download Model): ```bash modelscope download --model Qwen/QwQ-32B-GGUF qwq-32b-q4_k_m.gguf --local_dir /data/vLLM/model/QwQ-32B-Q4_1 ``` ### 🐛 Describe the bug CUDA Out of Memory Error when Running vLLM with RTX 4090 **Body:** I am experiencing a CUDA out of memory error while trying to run the following command on my server with an RTX 4090 (24GB) GPU: ![Image](https://github.com/user-attachments/assets/371704b0-535e-469a-ac6b-44894778021d) ## I run the command in the terminal: ```bash vllm serve /data...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: onda create -n vllm python=3.12 -y conda activate vllm ``` CUDA 版本 (CUDA Version): 12.2 使用最新的预编译包方案 (Use the latest precompiled package solution): ```bash pip install vllm --pre --extra-index-url https://wheels.vllm.ai/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: nt): ```bash conda create -n vllm python=3.12 -y conda activate vllm ``` CUDA 版本 (CUDA Version): 12.2 使用最新的预编译包方案 (Use the latest precompiled package solution): ```bash pip install vllm --pre --extra-index-url https://w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: The qwq-32b-q4_k_m.gguf quantized model is not supported. bug;stale ### Your current environment 创建环境 (Create Environment): ```bash conda create -n vllm python=3.12 -y conda activate vllm ``` CUDA 版本 (CUDA Versio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: OS:** Linux ### Output Log: ``` INFO 03-18 16:00:29 [cuda.py:285] Using Flash Attention backend. INFO 03-18 16:00:30 [parallel_state.py:948] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0 INFO 03-...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ctivation peak memory takes 1.40GiB; the rest of the memory reserved for KV Cache is 1.31GiB. INFO 03-18 16:01:12 [executor_base.py:111] # cuda blocks: 334, # CPU blocks: 1024 INFO 03-18 16:01:12 [executor_base.py:116]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
