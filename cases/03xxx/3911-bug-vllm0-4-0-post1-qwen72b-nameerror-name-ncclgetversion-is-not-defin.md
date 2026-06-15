# vllm-project/vllm#3911: [Bug]: vllm0.4.0 post1，双卡加载qwen72b报错：NameError: name 'ncclGetVersion' is not defined

| 字段 | 值 |
| --- | --- |
| Issue | [#3911](https://github.com/vllm-project/vllm/issues/3911) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm0.4.0 post1，双卡加载qwen72b报错：NameError: name 'ncclGetVersion' is not defined

### Issue 正文摘录

### Your current environment 环境Python 3.10.0，torch2.1.2+cu118 ### 🐛 Describe the bug vllm0.4.0 post1，双卡加载qwen72b报错：NameError: name 'ncclGetVersion' is not defined

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: vllm0.4.0 post1，双卡加载qwen72b报错：NameError: name 'ncclGetVersion' is not defined bug ### Your current environment 环境Python 3.10.0，torch2.1.2+cu118 ### 🐛 Describe the bug vllm0.4.0 post1，双卡加载qwen72b报错：NameError: name...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: vllm0.4.0 post1，双卡加载qwen72b报错：NameError: name 'ncclGetVersion' is not defined bug ### Your current environment 环境Python 3.10.0，torch2.1.2+cu118 ### 🐛 Describe the bug vllm0.4.0 post1，双卡加载qwen72b报错：NameError: name...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
