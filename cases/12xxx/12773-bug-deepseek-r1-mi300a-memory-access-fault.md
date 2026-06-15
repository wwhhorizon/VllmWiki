# vllm-project/vllm#12773: [Bug]: Deepseek R1 MI300A Memory access fault

| 字段 | 值 |
| --- | --- |
| Issue | [#12773](https://github.com/vllm-project/vllm/issues/12773) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek R1 MI300A Memory access fault

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I can run llama 1B, 8B, 408B fine on multiple nodes (each with 4 MI300A). When I try running deepseed R1, the model gets loaded then fails like below. ``` INFO 02-05 09:11:53 model_runner.py:1118] Loading model weights took 18.4303 GB (RayWorkerWrapper pid=1039658) INFO 02-05 09:11:53 model_runner.py:1118] Loading model weights took 18.4303 GB (RayWorkerWrapper pid=394715, ip=10.65.144.3) DEBUG 02-05 09:08:18 shm_broadcast.py:282] Connecting to tcp://127.0.0.1:49717 [repeated 23x across cluster] (RayWorkerWrapper pid=394716, ip=10.65.144.3) INFO 02-05 09:08:19 rocm.py:121] Using Triton MLA backend. [repeated 31x across cluster] (RayWorkerWrapper pid=441438, ip=10.65.144.7) DEBUG 02-05 09:08:23 config.py:3434] disabled custom ops: Counter() [repeated 31x across cluster] (RayWorkerWrapper pid=394716, ip=10.65.144.3) DEBUG 02-05 09:08:18 shm_broadcast.py:217] Binding to tcp://127.0.0.1:49717 [repeated 6x across cluster] (RayWorkerWrapper pid=394716, ip=10.65.144.3) INFO 02-05 09:08:18 shm_broadcast.py:258] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1, 2, 3], buffer_handle=(3, 4194304,...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Deepseek R1 MI300A Memory access fault bug;rocm;stale ### Your current environment ### 🐛 Describe the bug I can run llama 1B, 8B, 408B fine on multiple nodes (each with 4 MI300A). When I try running deepseed R1,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: O 02-05 09:08:19 model_runner.py:1113] Starting to load model /lus/home/BCINES/dci/malaboeuf/repository.backedup/Inferencing/HF_HOME/hub/models--deepseek-ai--DeepSeek-R1/snapshots/5dde110d1a9ee857b90a6710b7138f9130ce6fa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: stale ### Your current environment ### 🐛 Describe the bug I can run llama 1B, 8B, 408B fine on multiple nodes (each with 4 MI300A). When I try running deepseed R1, the model gets loaded then fails like below. ``` INFO 0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: apper pid=394716, ip=10.65.144.3) INFO 02-05 09:08:19 rocm.py:121] Using Triton MLA backend. [repeated 31x across cluster] (RayWorkerWrapper pid=441438, ip=10.65.144.7) DEBUG 02-05 09:08:23 config.py:3434] disabled cust...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: er] (RayWorkerWrapper pid=394715, ip=10.65.144.3) WARNING 02-05 09:14:42 fp8_utils.py:436] Using default W8A8 Block FP8 kernel config. Performance might be sub-optimal! Config file not found at /lus/home/BCINES/dci/mala...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
