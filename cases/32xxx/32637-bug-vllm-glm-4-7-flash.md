# vllm-project/vllm#32637: [Bug]: vllm启动GLM-4.7-Flash失败

| 字段 | 值 |
| --- | --- |
| Issue | [#32637](https://github.com/vllm-project/vllm/issues/32637) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm启动GLM-4.7-Flash失败

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 显卡：A800 docker run -it --gpus '"device=1,7"' --network host --ipc=host --shm-size=16g -v /raid/models/GLM-4.7-Flash:/models/GLM-4.7-Flash --entrypoint /bin/bash vllm/vllm-openai:nightly 进入容器后，使用以下命令启动模型： vllm serve GLM-4.7-Flash \ --tensor-parallel-size 2 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --served-model-name GLM-4.7-Flash \ --port 8002 \ --max-model-len 32768 \ --gpu-memory-utilization 0.8 报错： (APIServer pid=212) pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig (APIServer pid=212) Value error, The checkpoint you are trying to load has model type `glm4_moe_lite` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. (APIServer pid=212) (APIServer pid=212) You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. I...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: '"device=1,7"' --network host --ipc=host --shm-size=16g -v /raid/models/GLM-4.7-Flash:/models/GLM-4.7-Flash --entrypoint /bin/bash vllm/vllm-openai:nightly 进入容器后，使用以下命令启动模型： vllm serve GLM-4.7-Flash \ --tensor-parallel-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ;stale ### Your current environment ### 🐛 Describe the bug 显卡：A800 docker run -it --gpus '"device=1,7"' --network host --ipc=host --shm-size=16g -v /raid/models/GLM-4.7-Flash:/models/GLM-4.7-Flash --entrypoint /bin/bash...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm启动GLM-4.7-Flash失败 bug;stale ### Your current environment ### 🐛 Describe the bug 显卡：A800 docker run -it --gpus '"device=1,7"' --network host --ipc=host --shm-size=16g -v /raid/models/GLM-4.7-Flash:/models/GLM-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: has model type `glm4_moe_lite` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. (APIServer pid=212) (A...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Value error, The checkpoint you are trying to load has model type `glm4_moe_lite` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
