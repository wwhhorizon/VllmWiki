# vllm-project/vllm#1698: baichuan2-13b A10 deploy

| 字段 | 值 |
| --- | --- |
| Issue | [#1698](https://github.com/vllm-project/vllm/issues/1698) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> baichuan2-13b A10 deploy

### Issue 正文摘录

hi there, I wonder how can users deploy a baichuan2-13b model on a single A10 gpu server, due to the limited gpu memory, we have to use quantization method, but it seems vllm now not support quantization method to deploy such models, If directly use the auto-awq method, seem not support baichuan as follows: File ~/miniconda3/envs/vllm/lib/python3.8/site-packages/awq/models/auto.py:24, in check_and_get_model_type(model_dir, trust_remote_code) 22 config = AutoConfig.from_pretrained(model_dir, trust_remote_code=trust_remote_code) 23 if config.model_type not in AWQ_CAUSAL_LM_MODEL_MAP.keys(): ---> 24 raise TypeError(f"{config.model_type} isn't supported yet.") 25 model_type = config.model_type 26 return model_type TypeError: baichuan isn't supported yet. does anyone have any solutions, thx ahead of time.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 2-13b A10 deploy hi there, I wonder how can users deploy a baichuan2-13b model on a single A10 gpu server, due to the limited gpu memory, we have to use quantization method, but it seems vllm now not support quantizatio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n a single A10 gpu server, due to the limited gpu memory, we have to use quantization method, but it seems vllm now not support quantization method to deploy such models, If directly use the auto-awq method, seem not su...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: loy a baichuan2-13b model on a single A10 gpu server, due to the limited gpu memory, we have to use quantization method, but it seems vllm now not support quantization method to deploy such models, If directly use the a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
