# vllm-project/vllm#1120: --download-dir is not strictly obeyed

| 字段 | 值 |
| --- | --- |
| Issue | [#1120](https://github.com/vllm-project/vllm/issues/1120) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> --download-dir is not strictly obeyed

### Issue 正文摘录

## Issue When using the `--download_dir` argument, the server modules (I only tested with them) still download and use files in the `~/.cache/` path. Note that the actual model file is not downloaded there, but the surrounding config files are. ## Expected Behaviour All file are downloaded to and used from the path provided by `--download_dir` ## STR ```bash rm -rf ~/.cache/huggingface/hub/models--facebook--opt-125m/ root@425b8da2809f:/# python -m vllm.entrypoints.api_server --host 0.0.0.0 --port 10102 --download-dir /models/ Downloading (…)lve/main/config.json: 100%|███████████████████████████| 651/651 [00:00 ../../blobs/2d74da6615135c58cf3cf9ad4cb11e7c613ff9e55fe658a47ab83b6c8d1174a9 ``` ```bash root@425b8da2809f:/# ls -latr ~/.cache/huggingface/hub/models--facebook--opt-125m/snapshots/27dcfa74d334bc871f3234de431e71c6eeba5dd6/ total 8 drwxr-xr-x 3 root root 4096 Sep 21 04:58 .. lrwxrwxrwx 1 root root 52 Sep 21 04:58 config.json -> ../../blobs/b3fb716a3024261980becb2382e31a3780985130 lrwxrwxrwx 1 root root 52 Sep 21 04:58 tokenizer_config.json -> ../../blobs/27c24ca9d908d0b678b20c698aeb9e950c44d865 lrwxrwxrwx 1 root root 52 Sep 21 04:58 vocab.json -> ../../blobs/0a39732b2d8be8e49...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ill download and use files in the `~/.cache/` path. Note that the actual model file is not downloaded there, but the surrounding config files are. ## Expected Behaviour All file are downloaded to and used from the path...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: x 1 root root 52 Sep 21 04:58 special_tokens_map.json -> ../../blobs/5dfa36546b8eddce0e04df3133c30df43fcc3828 ```
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 789c48f0cb3ec53eda48b7be36cc lrwxrwxrwx 1 root root 52 Sep 21 04:58 special_tokens_map.json -> ../../blobs/5dfa36546b8eddce0e04df3133c30df43fcc3828 ```
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ue When using the `--download_dir` argument, the server modules (I only tested with them) still download and use files in the `~/.cache/` path. Note that the actual model file is not downloaded there, but the surroundin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
