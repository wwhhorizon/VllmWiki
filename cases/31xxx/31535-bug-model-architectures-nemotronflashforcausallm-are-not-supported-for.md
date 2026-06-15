# vllm-project/vllm#31535: [Bug]: Model architectures ['NemotronFlashForCausalLM'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#31535](https://github.com/vllm-project/vllm/issues/31535) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['NemotronFlashForCausalLM'] are not supported for now.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug i downloaded [Nemotron-Flash-3B-Instruct](https://modelscope.cn/models/nv-community/Nemotron-Flash-3B-Instruct) and used below docker command to run ```bash sudo docker run --rm --runtime nvidia --gpus all \ -v /mnt/c/wslshare/Nemotron-Flash-3B-Instruct:/model \ -p 8000:8000 --ipc=host \ docker.m.daocloud.io/vllm/vllm-openai:nightly-96142f209453a381fcaf9d9d010bbf8711119a77 \ /model \ --api-key mytoken \ --enforce-eager \ --max-model-len 17904 \ --gpu-memory-utilization 0.90 \ --max-num-seqs 3 \ --enable-prefix-caching \ --disable-log-requests \ --tensor-parallel-size 1 \ --trust_remote_code ``` and shows error(part of) > (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/arg_utils.py", line 1204, in create_model_config > (APIServer pid=1) return ModelConfig( > (APIServer pid=1) ^^^^^^^^^^^^ > (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/pydantic/_internal/_dataclasses.py", line 121, in __init__ > (APIServer pid=1) s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s) > (APIServer pid=1) pydantic_core._pydantic_core.ValidationError: 1 validation error for Mo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Model architectures ['NemotronFlashForCausalLM'] are not supported for now. bug ### Your current environment ### 🐛 Describe the bug i downloaded [Nemotron-Flash-3B-Instruct](https://modelscope.cn/models/nv-commun...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lscope.cn/models/nv-community/Nemotron-Flash-3B-Instruct) and used below docker command to run ```bash sudo docker run --rm --runtime nvidia --gpus all \ -v /mnt/c/wslshare/Nemotron-Flash-3B-Instruct:/model \ -p 8000:80...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Model architectures ['NemotronFlashForCausalLM'] are not supported for now. bug ### Your current environment ### 🐛 Describe the bug i downloaded [Nemotron-Flash-3B-Instruct](https://modelscope.cn/models/nv-commun...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: alLM'] are not supported for now. Supported architectures: dict_keys(['AfmoeForCausalLM', 'ApertusForCausalLM', 'AquilaModel', 'AquilaForCausalLM', 'ArceeForCausalLM', 'ArcticForCausalLM', 'BaiChuanForCausalLM', 'Baichu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ion 0.90 \ --max-num-seqs 3 \ --enable-prefix-caching \ --disable-log-requests \ --tensor-parallel-size 1 \ --trust_remote_code ``` and shows error(part of) > (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
