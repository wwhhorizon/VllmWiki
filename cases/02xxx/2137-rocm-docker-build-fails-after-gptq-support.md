# vllm-project/vllm#2137: ROCm Docker build fails after GPTQ support

| 字段 | 值 |
| --- | --- |
| Issue | [#2137](https://github.com/vllm-project/vllm/issues/2137) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 | install |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ROCm Docker build fails after GPTQ support

### Issue 正文摘录

hey, i just noticed the recent most push fails on rocm https://github.com/vllm-project/vllm/blob/b81a6a6bb342d7b9166a1c7a6b69507fb53ff33e/setup.py#L222 can you add this line in the setup.py along with awq quantization like so https://github.com/vllm-project/vllm/blob/b81a6a6bb342d7b9166a1c7a6b69507fb53ff33e/setup.py#L228 If this feature is suppose to support rocm can you also check as hipify is not able to import #include Thank you _Originally posted by @hex-plex in https://github.com/vllm-project/vllm/issues/916#issuecomment-1858585757_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ROCm Docker build fails after GPTQ support hey, i just noticed the recent most push fails on rocm https://github.com/vllm-project/vllm/blob/b81a6a6bb342d7b9166a1c7a6b69507fb53ff33e/setup.py#L222 can you add this line in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ROCm Docker build fails after GPTQ support hey, i just noticed the recent most push fails on rocm https://github.com/vllm-project/vllm/blob/b81a6a6bb342d7b9166a1c7a6b69507fb53ff33e/setup.py#L222 can you add this line i
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 33e/setup.py#L222 can you add this line in the setup.py along with awq quantization like so https://github.com/vllm-project/vllm/blob/b81a6a6bb342d7b9166a1c7a6b69507fb53ff33e/setup.py#L228 If this feature is suppose to...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
