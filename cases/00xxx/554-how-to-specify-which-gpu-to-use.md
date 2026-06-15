# vllm-project/vllm#554: How to specify which gpu to use?

| 字段 | 值 |
| --- | --- |
| Issue | [#554](https://github.com/vllm-project/vllm/issues/554) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to specify which gpu to use?

### Issue 正文摘录

If I have multiple GPUs, how can I specify which GPU to use individually? Previously, I used `'device_map': 'sequential'` with `accelerate` to control this. Now, with `vllm_engine`, is there a similar functionality available?" exp. if i want to specify the `gpu1` instead of `gpu0`,because they are not same type of card.i will write like this: ```python model_kwargs = {"torch_dtype": torch.float16, 'device_map': 'sequential'} ``` Then, I manually set the available memory of `device0` to 0, with the purpose of using `device1`: ``` GPU_max_memory: {0: '0GiB', 1: '40GiB'} ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: me type of card.i will write like this: ```python model_kwargs = {"torch_dtype": torch.float16, 'device_map': 'sequential'} ``` Then, I manually set the available memory of `device0` to 0, with the purpose of using `dev...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: How to specify which gpu to use? If I have multiple GPUs, how can I specify which GPU to use individually? Previously, I used `'device_map': 'sequential'` with `accelerate` to control this. Now, with `vllm_engine`, is t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: because they are not same type of card.i will write like this: ```python model_kwargs = {"torch_dtype": torch.float16, 'device_map': 'sequential'} ``` Then, I manually set the available memory of `device0` to 0, with th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
