# vllm-project/vllm#2422: Phi-2 Broken

| 字段 | 值 |
| --- | --- |
| Issue | [#2422](https://github.com/vllm-project/vllm/issues/2422) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Phi-2 Broken

### Issue 正文摘录

I've tried pip's version of `vllm`, and github `master`. I've tried pip's version of `transformers` and github `master`. I've tried an older `git clone` of HF's `microsoft/phi-2`, and then `git cloned` it anew. When I try running it in python code, or in server mode, I get this error: ```sh File "/home/mobius/_/lib/vllm/vllm/model_executor/models/phi_1_5.py", line 219, in __init__ self.h = nn.ModuleList([ File "/home/mobius/_/lib/vllm/vllm/model_executor/models/phi_1_5.py", line 220, in PhiLayer(config, linear_method) File "/home/mobius/_/lib/vllm/vllm/model_executor/models/phi_1_5.py", line 186, in __init__ eps=config.layer_norm_epsilon) File "/home/mobius/_/lib/transformers/src/transformers/configuration_utils.py", line 265, in __getattribute__ return super().__getattribute__(key) AttributeError: 'PhiConfig' object has no attribute 'layer_norm_epsilon'. Did you mean: 'layer_norm_eps'? ``` If I go into the `vllm` code and fix that, I now get: ```sh File "/home/user/_/lib/vllm/vllm/model_executor/models/phi_1_5.py", line 192, in __init__ self.mixer = PhiAttention(config, linear_method) File "/home/user/_/lib/vllm/vllm/model_executor/models/phi_1_5.py", line 116, in __init__ rotary...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: f `transformers` and github `master`. I've tried an older `git clone` of HF's `microsoft/phi-2`, and then `git cloned` it anew. When I try running it in python code, or in server mode, I get this error: ```sh File "/hom...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Phi-2 Broken I've tried pip's version of `vllm`, and github `master`. I've tried pip's version of `transformers` and github `master`. I've tried an older `git clone` of HF's `microsoft/phi-2`, and then `git cloned` it a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
