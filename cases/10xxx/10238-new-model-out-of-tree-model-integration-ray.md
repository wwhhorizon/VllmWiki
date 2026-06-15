# vllm-project/vllm#10238: [New Model]: 采用 Out-of-Tree Model Integration 方式注册新模型在启用多卡 Ray 模式下的注册信息丢失的问题

| 字段 | 值 |
| --- | --- |
| Issue | [#10238](https://github.com/vllm-project/vllm/issues/10238) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: 采用 Out-of-Tree Model Integration 方式注册新模型在启用多卡 Ray 模式下的注册信息丢失的问题

### Issue 正文摘录

1、自定义模型的注册方式是Out-of-Tree Model Integration，即不改动vllm源码的方式下注册了新模型Qwen2GotForCausalLM ![image](https://github.com/user-attachments/assets/7694d9ca-48a1-4a8e-bc27-7570f1cff968) 参考自：https://docs.vllm.ai/en/latest/models/adding_model.html 2、一机多GPU=2下启动vllm api_server使用时（vllm版本0.6.3.post1）： （1）--tensor-parallel-size 2 + 默认的 --distributed-executor-backend mp 模式服务顺利启动，新模型也一切工作正常 （2）但如果 --tensor-parallel-size 2 + --distributed-executor-backend ray 模式下server就会启动不了，重点报错信息如下： ... (RayWorkerWrapper pid=52112) ERROR 11-12 08:45:40 worker_base.py:464] return ModelRegistry.resolve_model_cls(architectures) (RayWorkerWrapper pid=52112) ERROR 11-12 08:45:40 worker_base.py:464] File "/home/vipuser/miniconda3/envs/gotv/lib/python3.10/site-packages/vllm/model_executor/models/registry.py", line 369, in resolve_model_cls (RayWorkerWrapper pid=52112) ERROR 11-12 08:45:40 worker_base.py:464] return self._raise_for_unsupported(architectures) (RayWorkerWrapper pid=52112) ERROR 11-12 08:45:40 worker_base.py:464] File "/home/vipuser/miniconda3/envs/gotv/lib/python3.10/site-packages/vllm/model_executor/models/registry.py", line 317, in _raise_for_unsupported (RayWorkerWrapper pid=52112) ERROR 11-12 08:45:40 work...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: 采用 Out-of-Tree Model Integration 方式注册新模型在启用多卡 Ray 模式下的注册信息丢失的问题 new-model 1、自定义模型的注册方式是Out-of-Tree Model Integration，即不改动vllm源码的方式下注册了新模型Qwen2GotForCausalLM ![image](https://github.com/user-attachments/asse...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 版本0.6.3.post1）： （1）--tensor-parallel-size 2 + 默认的 --distributed-executor-backend mp 模式服务顺利启动，新模型也一切工作正常 （2）但如果 --tensor-parallel-size 2 + --distributed-executor-backend ray 模式下server就会启动不了，重点报错信息如下： ... (RayWorkerWrappe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 08:45:40 worker_base.py:464] return ModelRegistry.resolve_model_cls(architectures) (RayWorkerWrapper pid=52112) ERROR 11-12 08:45:40 worker_base.py:464] File "/home/vipuser/miniconda3/envs/gotv/lib/python3.10/site-packa...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ', 'ArcticForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', ....] 貌似在Ray启动后进程应该切换了，导致已注册模型列表里又没有了Out-of-Tree方式添加的自定义模型了 请问这是一个BUG还是模型注册时哪里有疏漏的问题？有没有什么解决办法？（不改动vllm源码）
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: sets/7694d9ca-48a1-4a8e-bc27-7570f1cff968) 参考自：https://docs.vllm.ai/en/latest/models/adding_model.html 2、一机多GPU=2下启动vllm api_server使用时（vllm版本0.6.3.post1）： （1）--tensor-parallel-size 2 + 默认的 --distributed-executor-backend...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
