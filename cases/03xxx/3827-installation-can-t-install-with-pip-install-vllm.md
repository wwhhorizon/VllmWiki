# vllm-project/vllm#3827: [Installation]: can‘t install with pip install vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#3827](https://github.com/vllm-project/vllm/issues/3827) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: can‘t install with pip install vllm

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ![image](https://github.com/vllm-project/vllm/assets/154483517/412bc386-e2db-41af-a160-2b28cee3e05c) ![image](https://github.com/vllm-project/vllm/assets/154483517/c52e48ab-ad8e-457c-8387-49b84de5293d) ### How you are installing vllm ```sh pip install -vvv vllm ``` ![image](https://github.com/vllm-project/vllm/assets/154483517/91c1b0b9-17e5-4c1a-94e4-4e2e5c993280) ![image](https://github.com/vllm-project/vllm/assets/154483517/1f197e93-b78a-49dd-8b1b-3b406af5a69f) ![image](https://github.com/vllm-project/vllm/assets/154483517/2770e9d6-3684-4626-a7b4-16c98b3d7cfe) ![image](https://github.com/vllm-project/vllm/assets/154483517/d6f96a5b-ae05-4439-99bf-2c2686009fc8) ![image](https://github.com/vllm-project/vllm/assets/154483517/1f771b8d-4ed6-4cd7-b471-db4f45c57260) ![image](https://github.com/vllm-project/vllm/assets/154483517/0aa64d21-1e75-4c05-af5d-74a53816a919)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: can‘t install with pip install vllm installation ### Your current environment ```text The output of `python collect_env.py` ``` ![image](https://github.com/vllm-project/vllm/assets/154483517/412bc386-e2db

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
