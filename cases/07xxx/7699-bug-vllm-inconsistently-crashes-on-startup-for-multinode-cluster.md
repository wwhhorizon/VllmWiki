# vllm-project/vllm#7699: [Bug]: vLLM inconsistently crashes on startup for multinode cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#7699](https://github.com/vllm-project/vllm/issues/7699) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM inconsistently crashes on startup for multinode cluster

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Description After calling `vllm serve`, vLLM begins initializing, then fails with an NCCL error during initialization with no additional information. Setting the following gives more information, but still no errors or warnings. ``` export NCCL_DEBUG=INFO export NCCL_DEBUG_SUBSYS=INIT,P2P,NET,GRAPH,ENV,TUNING ``` # Command ``` # Start ray on head and worker nodes ray start ... ... # vllm serve on head node vllm serve "${HF_HOME}/hub/models--${SNAPSHOT_DIR}/snapshots/$SNAPSHOT" \ --tensor-parallel-size=$tensor_parallel \ --distributed-executor-backend=ray \ --disable-custom-all-reduce \ 2>&1 | tee "${TMPDIR}api_server.log" & ``` # Failed Trace ``` ======== Autoscaler status: 2024-08-19 21:32:14.787892 ======== Node status --------------------------------------------------------------- Active: 1 node_e161bb4b4023b8fe68152672794804629f3995241b7cc60fd9fe8ae2 1 node_0fcb74c428a1f8e66d45d27879bfc50cc73e80bf268f27ded6284b5c Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/128.0 CPU 0.0/8.0 GPU 0B/685.33GiB memory 0B/297.70GiB object_store_me...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: /297.70GiB object_store_memory Demands: (no resource demands) Node: 0: Waiting for vLLM API server to start... INFO 08-19 21:32:26 api_server.py:339] vLLM API server version 0.5.4 INFO 08-19 21:32:26 api_server.py:340]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: then fails with an NCCL error during initialization with no additional information. Setting the following gives more information, but still no errors or warnings. ``` export NCCL_DEBUG=INFO export NCCL_DEBUG_SUBSYS=INIT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 1 | tee "${TMPDIR}api_server.log" & ``` # Failed Trace ``` ======== Autoscaler status: 2024-08-19 21:32:14.787892 ======== Node status --------------------------------------------------------------- Active: 1 node_e161b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: --tensor-parallel-size=$tensor_parallel \ --distributed-executor-backend=ray \ --disable-custom-all-reduce \ 2>&1 | tee "${TMPDIR}api_server.log" & ``` # Failed Trace ``` ======== Autoscaler status: 2024-08-19 21:32:14....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: erver to start... INFO 08-19 21:32:26 api_server.py:339] vLLM API server version 0.5.4 INFO 08-19 21:32:26 api_server.py:340] args: Namespace(model_tag='/root/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-8B...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
