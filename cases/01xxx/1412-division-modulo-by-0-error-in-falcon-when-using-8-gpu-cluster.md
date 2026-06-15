# vllm-project/vllm#1412: Division/modulo by 0 error in Falcon when using >8 gpu cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#1412](https://github.com/vllm-project/vllm/issues/1412) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 | debug |
| Operator 关键词 | attention;cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Division/modulo by 0 error in Falcon when using >8 gpu cluster

### Issue 正文摘录

Hi vllm, We're doing some benchmarking for various configurations. Our cluster setup is a 2-node, 16 gpu L40 running ray. For the 40B Falcon model I'm not able to run this using 16 gpus (2 nodes) but we are able to run this same workload using 2,4,8 gpus and the 40B Falcon model). The error is a division by 0 on the 16 gpu but not on the 8 gpu. Here is a brief stack trace/logs for both scenarios Here is `tensor_parallel_size=8` ```bash INFO 2023-10-18 16:22:35,133 run.py:137 unknown_model_name:unknown_model_version Hello! logging initialized, starting up... INFO 2023-10-18 16:22:35,133 run.py:138 unknown_model_name:unknown_model_version Git commit of model: unknown_git_commit INFO 2023-10-18 16:22:35,133 run.py:139 unknown_model_name:unknown_model_version Git commit of cuda torch base: unknown_git_commit INFO 2023-10-18 16:22:35,653 run.py:143 unknown_model_name:unknown_model_version Compute device available: cuda 2023-10-18 16:22:35,930 INFO worker.py:1458 -- Connecting to existing Ray cluster at address: 172.18.220.54:6379... 2023-10-18 16:22:35,936 INFO worker.py:1642 -- Connected to Ray cluster. INFO 2023-10-18 16:23:50,962 run.py:166 unknown_model_name:unknown_model_version S...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ███| 1/1 [00:01 chat_en = ChatEn(ngpu=args.ngpu) File "/home/cirrascale/run.py", line 162, in __init__ self.model = LLM(model=self.model_path, tensor_parallel_size=self.n_gpu) File "/home/cirrascale/.local/share/virtual...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing >8 gpu cluster Hi vllm, We're doing some benchmarking for various configurations. Our cluster setup is a 2-node, 16 gpu L40 running ray. For the 40B Falcon model I'm not able to run this using 16 gpus (2 nodes) but...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: INFO 2023-10-18 16:22:35,133 run.py:137 unknown_model_name:unknown_model_version Hello! logging initialized, starting up... INFO 2023-10-18 16:22:35,133 run.py:138 unknown_model_name:unknown_model_version Git commit of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 35,133 run.py:139 unknown_model_name:unknown_model_version Git commit of cuda torch base: unknown_git_commit INFO 2023-10-18 16:22:35,653 run.py:143 unknown_model_name:unknown_model_version Compute device available: cud...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e config.json for falcon we have in the cluster: ```bash { "alibi": false, "apply_residual_connection_post_layernorm": false, "architectures": [ "FalconForCausalLM" ], "attention_dropout": 0.0, "auto_map": { "AutoConfig...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
