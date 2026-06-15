# vllm-project/vllm#3682: undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

| 字段 | 值 |
| --- | --- |
| Issue | [#3682](https://github.com/vllm-project/vllm/issues/3682) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

### Issue 正文摘录

I installed vllm and proceeded with import vllm, but the error occurred as above. i dont know how to solve this problem. **installation environment** is as follows. > vllm : 0.3.3 cuda : 12.1 python : 3.10.6 torch : 2.1.2 transformers : 4.38.2 transformer-engine : 0.10.0 accelerate : 0.23.0 xformers : 0.0.23.post1 Please help out if anyone solved this issue.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE documentation I installed vllm and proceeded with import vllm, but the error occurred as above. i dont know how to
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s problem. **installation environment** is as follows. > vllm : 0.3.3 cuda : 12.1 python : 3.10.6 torch : 2.1.2 transformers : 4.38.2 transformer-engine : 0.10.0 accelerate : 0.23.0 xformers : 0.0.23.post1 Please help o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
