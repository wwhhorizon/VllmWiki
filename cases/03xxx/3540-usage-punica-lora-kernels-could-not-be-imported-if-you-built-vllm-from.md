# vllm-project/vllm#3540: [Usage]: punica LoRA kernels could not be imported. If you built vLLM from source, make sure VLLM_INSTALL_PUNICA_KERNELS=1 env var was set.

| 字段 | 值 |
| --- | --- |
| Issue | [#3540](https://github.com/vllm-project/vllm/issues/3540) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: punica LoRA kernels could not be imported. If you built vLLM from source, make sure VLLM_INSTALL_PUNICA_KERNELS=1 env var was set.

### Issue 正文摘录

When I was using yi and qwen, due to the error When using LoRA, vocab size must be 32000 >= vocab_size <= 33024, I modified the source code of bgmv_config.h and rebuilt it using python setup.py install. Now the above error is prompted. , but I added it to my code os.environ['VLLM_INSTALL_PUNICA_KERNELS'] = "1" How should I modify it to work properly

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: punica LoRA kernels could not be imported. If you built vLLM from source, make sure VLLM_INSTALL_PUNICA_KERNELS=1 env var was set. usage When I was using yi and qwen, due to the error When using LoRA, vocab siz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _INSTALL_PUNICA_KERNELS=1 env var was set. usage When I was using yi and qwen, due to the error When using LoRA, vocab size must be 32000 >= vocab_size <= 33024, I modified the source code of bgmv_config.h and rebuilt i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
