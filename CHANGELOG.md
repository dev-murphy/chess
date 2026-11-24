# Changelog

## [1.2.1](https://github.com/dev-murphy/yaadchess/compare/v1.2.0...v1.2.1) (2026-11-24)

### Bug Fixes

* **build:** make packaged executables start and load the UI ([9c04c08](https://github.com/dev-murphy/yaadchess/commit/9c04c082a7e7c2183036f5747b8f14151e3b9b5e))

## [1.2.0](https://github.com/dev-murphy/yaadchess/releases/tag/v1.2.0) (2026-11-23)

### Features

* end the game on checkmate, stalemate or draw ([aa706d6](https://github.com/dev-murphy/yaadchess/commit/aa706d67b3f86d378f18fefb99dabb05b59b1916))

### Bug Fixes

* **ui:** assert non-null piece in Board template ([d1c8ca5](https://github.com/dev-murphy/yaadchess/commit/d1c8ca5a24331211f2aa77110e8917a353343dd5))

### Continuous Integration

* build executables and attach them to GitHub releases ([88b5e3f](https://github.com/dev-murphy/yaadchess/commit/88b5e3ff22f1f2cf4323f5cbfc394acd58248ed9))
* extract release notes from CHANGELOG.md ([4836da7](https://github.com/dev-murphy/yaadchess/commit/4836da7c4551d9783f2c4e646fd4d026dc77538d))


## [1.2.0](https://github.com/dev-murphy/yaadchess/compare/v1.1.0...v1.2.0) (2026-11-23)

### Features

* end the game on checkmate, stalemate or draw ([aa706d6](https://github.com/dev-murphy/yaadchess/commit/aa706d67b3f86d378f18fefb99dabb05b59b1916))

### Bug Fixes

* **ui:** assert non-null piece in Board template ([d1c8ca5](https://github.com/dev-murphy/yaadchess/commit/d1c8ca5a24331211f2aa77110e8917a353343dd5))

### Continuous Integration

* build executables and attach them to GitHub releases ([88b5e3f](https://github.com/dev-murphy/yaadchess/commit/88b5e3ff22f1f2cf4323f5cbfc394acd58248ed9))
* extract release notes from CHANGELOG.md ([4836da7](https://github.com/dev-murphy/yaadchess/commit/4836da7c4551d9783f2c4e646fd4d026dc77538d))

## [1.1.0](https://github.com/dev-murphy/yaadchess/releases/tag/v1.1.0) (2026-11-23)

### Features

* implement PlayerIndicator component ([4dc008f](https://github.com/dev-murphy/yaadchess/commit/4dc008f5ad2da7c5884cd756194481a5b5a06a09))

### Code Refactors

* update how version is accessed and remove extra spaces ([8d51201](https://github.com/dev-murphy/yaadchess/commit/8d512015339c0169973d6a3e1306f3b70b6603c7))

### Miscellaneous

* add side_to_move to chess engine api response ([fd1185a](https://github.com/dev-murphy/yaadchess/commit/fd1185a8069213bbc86642b13c742520efb060b2))

### Continuous Integration

* add changelog change to Github release ([1b1299d](https://github.com/dev-murphy/yaadchess/commit/1b1299dc8761c3f028777d8e1fa94a979545f6b3))

### Styles

* add fonts and favicon to the UI project ([b1ca2c3](https://github.com/dev-murphy/yaadchess/commit/b1ca2c3d09e61e947740f033d07f4388ee8c3c61))


## [1.1.0](https://github.com/dev-murphy/yaadchess/compare/v1.0.1...v1.1.0) (2026-11-23)

### Features

* implement PlayerIndicator component ([4dc008f](https://github.com/dev-murphy/yaadchess/commit/4dc008f5ad2da7c5884cd756194481a5b5a06a09))

### Code Refactors

* update how version is accessed and remove extra spaces ([8d51201](https://github.com/dev-murphy/yaadchess/commit/8d512015339c0169973d6a3e1306f3b70b6603c7))

### Miscellaneous

* add side_to_move to chess engine api response ([fd1185a](https://github.com/dev-murphy/yaadchess/commit/fd1185a8069213bbc86642b13c742520efb060b2))

### Continuous Integration

* add changelog change to Github release ([1b1299d](https://github.com/dev-murphy/yaadchess/commit/1b1299dc8761c3f028777d8e1fa94a979545f6b3))

### Styles

* add fonts and favicon to the UI project ([b1ca2c3](https://github.com/dev-murphy/yaadchess/commit/b1ca2c3d09e61e947740f033d07f4388ee8c3c61))

## [1.0.1](https://github.com/dev-murphy/yaadchess/releases/tag/v1.0.1) (2026-11-23)

### Bug Fixes

* fix typo, add Github bot user info and remove redundancies ([4d9b7d7](https://github.com/dev-murphy/yaadchess/commit/4d9b7d7e3bd7d232b77546850e4a2c33ae96ed1a))


## [1.0.1](https://github.com/dev-murphy/yaadchess/compare/v1.0.0...v1.0.1) (2026-11-23)

### Bug Fixes

* fix typo, add Github bot user info and remove redundancies ([4d9b7d7](https://github.com/dev-murphy/yaadchess/commit/4d9b7d7e3bd7d232b77546850e4a2c33ae96ed1a))

## [1.0.0](https://github.com/dev-murphy/yaadchess/releases/tag/v1.0.0) (2026-11-23)

### Features

* complete basic game UI and functionality ([5e460b0](https://github.com/dev-murphy/yaadchess/commit/5e460b012db0dd07115fea2276a85164e8723398))

### Code Refactors

* update api make_move function to return valid_move and state of the game ([8560c2f](https://github.com/dev-murphy/yaadchess/commit/8560c2fc915fc214e296ba8d9d92531ea0929d00))

### Miscellaneous

* fix FEN function, update setPosition function and add sync board function ([845ee7b](https://github.com/dev-murphy/yaadchess/commit/845ee7b932c17ba9ca44f6181a1ac92433adefc7))
* match the return types for API functions ([14824e4](https://github.com/dev-murphy/yaadchess/commit/14824e4c60ab0a10d82340677589a1bf3b7ce49d))
* add function to get board position from mouse coords and engine coords from board coords ([dcf1420](https://github.com/dev-murphy/yaadchess/commit/dcf142033a007218f055bc06bbe46c1e1b8ce156))
* add auto-import for composables ([d52540d](https://github.com/dev-murphy/yaadchess/commit/d52540de583c255bfc56b9cc53006580b294179f))
* create basic util to create fen notation and board grid representation ([399bc03](https://github.com/dev-murphy/yaadchess/commit/399bc035e0fba924040f2de7f05cb368b7ed0d89))

### Continuous Integration

* allow for breaking chages using exclamation signs ([de7033b](https://github.com/dev-murphy/yaadchess/commit/de7033ba1b657b4112bcb35c1aa04934705e65ca))
* create Github release based on the tags made ([e41d3da](https://github.com/dev-murphy/yaadchess/commit/e41d3daadecdd149489873b9cb8632a5e53f8ae4))


## [1.0.0](https://github.com/dev-murphy/yaadchess/compare/v0.11.1...v1.0.0) (2026-11-23)

### Features

* complete basic game UI and functionality ([5e460b0](https://github.com/dev-murphy/yaadchess/commit/5e460b012db0dd07115fea2276a85164e8723398))

### Code Refactors

* update api make_move function to return valid_move and state of the game ([8560c2f](https://github.com/dev-murphy/yaadchess/commit/8560c2fc915fc214e296ba8d9d92531ea0929d00))

### Miscellaneous

* fix FEN function, update setPosition function and add sync board function ([845ee7b](https://github.com/dev-murphy/yaadchess/commit/845ee7b932c17ba9ca44f6181a1ac92433adefc7))
* match the return types for API functions ([14824e4](https://github.com/dev-murphy/yaadchess/commit/14824e4c60ab0a10d82340677589a1bf3b7ce49d))
* add function to get board position from mouse coords and engine coords from board coords ([dcf1420](https://github.com/dev-murphy/yaadchess/commit/dcf142033a007218f055bc06bbe46c1e1b8ce156))
* add auto-import for composables ([d52540d](https://github.com/dev-murphy/yaadchess/commit/d52540de583c255bfc56b9cc53006580b294179f))
* create basic util to create fen notation and board grid representation ([399bc03](https://github.com/dev-murphy/yaadchess/commit/399bc035e0fba924040f2de7f05cb368b7ed0d89))

### Continuous Integration

* allow for breaking chages using exclamation signs ([de7033b](https://github.com/dev-murphy/yaadchess/commit/de7033ba1b657b4112bcb35c1aa04934705e65ca))
* create Github release based on the tags made ([e41d3da](https://github.com/dev-murphy/yaadchess/commit/e41d3daadecdd149489873b9cb8632a5e53f8ae4))

## [0.11.1](https://github.com/dev-murphy/yaadchess/releases/tag/v0.11.1) (2026-11-21)

### Bug Fixes

* remove `$` typo error ([1bb9e65](https://github.com/dev-murphy/yaadchess/commit/1bb9e65b479b72a96b8384baffd74b127cd9ab0a))
* reset other variables for special moves, side_to_move and move_log ([27ba16d](https://github.com/dev-murphy/yaadchess/commit/27ba16df8aa19d5cb91f758fe778abb1c09a56c8))
* add promotion type to make_move function in api class ([17c50fb](https://github.com/dev-murphy/yaadchess/commit/17c50fb38e5aaaf98a00614f1c130cc9a7a5f4d8))
* add en passant param in pseudo-legal moves and add get_king_moves functions ([af34261](https://github.com/dev-murphy/yaadchess/commit/af34261a8a8073ac160d74f2d12181c1fa6e11d1))

### Miscellaneous

* implement all special moves and mark it as done ([83921c7](https://github.com/dev-murphy/yaadchess/commit/83921c76b687001275d568121bff16b5d131b119))
* add variables for special moves like castling, en passant and promotion ([f6cafd4](https://github.com/dev-murphy/yaadchess/commit/f6cafd416cb78ca8c370b83ea99ac24bbed683c3))
* add castling rights and moves when getting king moves ([fa729d7](https://github.com/dev-murphy/yaadchess/commit/fa729d7823d017f1a765e9df6d819d748bd0aacb))
* add en passant params and check to get_pawn_attacks function ([9fccdca](https://github.com/dev-murphy/yaadchess/commit/9fccdcada5a5f4be9f53ef09e021f408ee956dee))


## [0.11.1](https://github.com/dev-murphy/yaadchess/compare/v0.11.0...v0.11.1) (2026-11-21)

### Bug Fixes

* remove `$` typo error ([1bb9e65](https://github.com/dev-murphy/yaadchess/commit/1bb9e65b479b72a96b8384baffd74b127cd9ab0a))
* reset other variables for special moves, side_to_move and move_log ([27ba16d](https://github.com/dev-murphy/yaadchess/commit/27ba16df8aa19d5cb91f758fe778abb1c09a56c8))
* add promotion type to make_move function in api class ([17c50fb](https://github.com/dev-murphy/yaadchess/commit/17c50fb38e5aaaf98a00614f1c130cc9a7a5f4d8))
* add en passant param in pseudo-legal moves and add get_king_moves functions ([af34261](https://github.com/dev-murphy/yaadchess/commit/af34261a8a8073ac160d74f2d12181c1fa6e11d1))

### Miscellaneous

* implement all special moves and mark it as done ([83921c7](https://github.com/dev-murphy/yaadchess/commit/83921c76b687001275d568121bff16b5d131b119))
* add variables for special moves like castling, en passant and promotion ([f6cafd4](https://github.com/dev-murphy/yaadchess/commit/f6cafd416cb78ca8c370b83ea99ac24bbed683c3))
* add castling rights and moves when getting king moves ([fa729d7](https://github.com/dev-murphy/yaadchess/commit/fa729d7823d017f1a765e9df6d819d748bd0aacb))
* add en passant params and check to get_pawn_attacks function ([9fccdca](https://github.com/dev-murphy/yaadchess/commit/9fccdcada5a5f4be9f53ef09e021f408ee956dee))

## [0.11.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.11.0) (2026-11-20)

### Features

* implement Chess API class, composables, typescript types ([8c4b404](https://github.com/dev-murphy/yaadchess/commit/8c4b404b3c4d5716016be18961ee8a3e5b3857aa))

### Code Refactors

* change has_legal_moves function to get_legal_moves ([671c5f6](https://github.com/dev-murphy/yaadchess/commit/671c5f64be5556ca2928dc6f02ffe4ca9f3714ef))


## [0.11.0](https://github.com/dev-murphy/yaadchess/compare/v0.10.1...v0.11.0) (2026-11-20)

### Features

* implement Chess API class, composables, typescript types ([8c4b404](https://github.com/dev-murphy/yaadchess/commit/8c4b404b3c4d5716016be18961ee8a3e5b3857aa))

### Code Refactors

* change has_legal_moves function to get_legal_moves ([671c5f6](https://github.com/dev-murphy/yaadchess/commit/671c5f64be5556ca2928dc6f02ffe4ca9f3714ef))

## [0.10.1](https://github.com/dev-murphy/yaadchess/releases/tag/v0.10.1) (2026-11-18)

### Bug Fixes

* remove "Yaad" from application title ([0c449b6](https://github.com/dev-murphy/yaadchess/commit/0c449b642a4e43ce0bae58377df782d4631dd37b))

### Documentation

* create TODO.md to track what's left ([6061733](https://github.com/dev-murphy/yaadchess/commit/6061733a30a8c710e1f7dc45ebc36d543fbcfa08))

### Miscellaneous

* change app logo ([81b4345](https://github.com/dev-murphy/yaadchess/commit/81b43455e7dd584c2aefd128597db8a21edfc884))


## [0.10.1](https://github.com/dev-murphy/yaadchess/compare/v0.10.0...v0.10.1) (2026-11-18)

### Bug Fixes

* remove "Yaad" from application title ([0c449b6](https://github.com/dev-murphy/yaadchess/commit/0c449b642a4e43ce0bae58377df782d4631dd37b))

### Documentation

* create TODO.md to track what's left ([6061733](https://github.com/dev-murphy/yaadchess/commit/6061733a30a8c710e1f7dc45ebc36d543fbcfa08))

### Miscellaneous

* change app logo ([81b4345](https://github.com/dev-murphy/yaadchess/commit/81b43455e7dd584c2aefd128597db8a21edfc884))

## [0.10.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.10.0) (2026-11-18)

### Features

* add move class to log all moves made and piece captured ([58b7209](https://github.com/dev-murphy/yaadchess/commit/58b7209fb1addd95346b1c48172f48e8b8301c63))
* implement functions to validate move based on piece type and color ([97d2bf4](https://github.com/dev-murphy/yaadchess/commit/97d2bf432f2f5539804eaaa75a1a0ed2d339a9c2))
* implement functions to generate all pseudo-legal moves for all pieces ([e3f2fd6](https://github.com/dev-murphy/yaadchess/commit/e3f2fd6cbc448058a4e4cd15020ff795b8b2fd4a))

### Bug Fixes

* resolve issues with piece position, is_in_check, piece color, board wrapping and other things ([9bd9327](https://github.com/dev-murphy/yaadchess/commit/9bd9327a72172be048688dca7d55d37c8f3d2709))

### Code Refactors

* repleace deppcopy is_valid_move function with making move in place ([0ed4685](https://github.com/dev-murphy/yaadchess/commit/0ed4685f3d374ed0a6cdb969d9598e03d4e21285))


## [0.10.0](https://github.com/dev-murphy/yaadchess/compare/v0.9.0...v0.10.0) (2026-11-18)

### Features

* add move class to log all moves made and piece captured ([58b7209](https://github.com/dev-murphy/yaadchess/commit/58b7209fb1addd95346b1c48172f48e8b8301c63))
* implement functions to validate move based on piece type and color ([97d2bf4](https://github.com/dev-murphy/yaadchess/commit/97d2bf432f2f5539804eaaa75a1a0ed2d339a9c2))
* implement functions to generate all pseudo-legal moves for all pieces ([e3f2fd6](https://github.com/dev-murphy/yaadchess/commit/e3f2fd6cbc448058a4e4cd15020ff795b8b2fd4a))

### Bug Fixes

* resolve issues with piece position, is_in_check, piece color, board wrapping and other things ([9bd9327](https://github.com/dev-murphy/yaadchess/commit/9bd9327a72172be048688dca7d55d37c8f3d2709))

### Code Refactors

* repleace deppcopy is_valid_move function with making move in place ([0ed4685](https://github.com/dev-murphy/yaadchess/commit/0ed4685f3d374ed0a6cdb969d9598e03d4e21285))

## [0.9.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.9.0) (2026-11-16)

### Features

* add move generator for knight and king attacks ([6101455](https://github.com/dev-murphy/yaadchess/commit/6101455d64defea67b89f403778c6a199418f588))
* set up chess class ([b259332](https://github.com/dev-murphy/yaadchess/commit/b2593323c10dbdc07e9b64ee510e988f4152142e))

### Bug Fixes

* fix rank typo and formatted code ([ed71f0c](https://github.com/dev-murphy/yaadchess/commit/ed71f0ca0479387cf1dd736df91cc7b6a7c21d5d))

### Code Refactors

* change class name to ChessBoard and fix white_occupied typo ([0948816](https://github.com/dev-murphy/yaadchess/commit/09488166797eab5e4e5f5a682783245befa2e9c9))
* formatted src/__init__.py file ([24e77a7](https://github.com/dev-murphy/yaadchess/commit/24e77a720720e4a96d99f76eed60e4abcf6803fb))

### Miscellaneous

* update uv.lock file ([9d7241a](https://github.com/dev-murphy/yaadchess/commit/9d7241af33cea107d2d6fbec7599b90c92770bde))

### Continuous Integration

* include uv.lock into version bump commit ([a3e4cd1](https://github.com/dev-murphy/yaadchess/commit/a3e4cd1fddee8c5f970f44b94874811294ef5ff3))


## [0.9.0](https://github.com/dev-murphy/yaadchess/compare/v0.8.0...v0.9.0) (2026-11-16)

### Features

* add move generator for knight and king attacks ([6101455](https://github.com/dev-murphy/yaadchess/commit/6101455d64defea67b89f403778c6a199418f588))
* set up chess class ([b259332](https://github.com/dev-murphy/yaadchess/commit/b2593323c10dbdc07e9b64ee510e988f4152142e))

### Bug Fixes

* fix rank typo and formatted code ([ed71f0c](https://github.com/dev-murphy/yaadchess/commit/ed71f0ca0479387cf1dd736df91cc7b6a7c21d5d))

### Code Refactors

* change class name to ChessBoard and fix white_occupied typo ([0948816](https://github.com/dev-murphy/yaadchess/commit/09488166797eab5e4e5f5a682783245befa2e9c9))
* formatted src/__init__.py file ([24e77a7](https://github.com/dev-murphy/yaadchess/commit/24e77a720720e4a96d99f76eed60e4abcf6803fb))

### Miscellaneous

* update uv.lock file ([9d7241a](https://github.com/dev-murphy/yaadchess/commit/9d7241af33cea107d2d6fbec7599b90c92770bde))

### Continuous Integration

* include uv.lock into version bump commit ([a3e4cd1](https://github.com/dev-murphy/yaadchess/commit/a3e4cd1fddee8c5f970f44b94874811294ef5ff3))

## [0.8.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.8.0) (2026-11-16)

### Features

* add sound effects for moving and capturig pieces ([76a0f8b](https://github.com/dev-murphy/yaadchess/commit/76a0f8b0d365c5d34c53b283c4c98602a6432833))

### Miscellaneous

* update uv.lock file ([2dcc323](https://github.com/dev-murphy/yaadchess/commit/2dcc323a9abbb8e54faec056e4831051ab8ef7a9))


## [0.8.0](https://github.com/dev-murphy/yaadchess/compare/v0.7.0...v0.8.0) (2026-11-16)

### Features

* add sound effects for moving and capturig pieces ([76a0f8b](https://github.com/dev-murphy/yaadchess/commit/76a0f8b0d365c5d34c53b283c4c98602a6432833))

### Miscellaneous

* update uv.lock file ([2dcc323](https://github.com/dev-murphy/yaadchess/commit/2dcc323a9abbb8e54faec056e4831051ab8ef7a9))

## [0.7.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.7.0) (2026-11-15)

### Features

* implementing moving pieces on the board ([f92d9c6](https://github.com/dev-murphy/yaadchess/commit/f92d9c697ad86af620c005d616796f2bcb19cac0))

### Miscellaneous

* resolve merge conflict ([054f184](https://github.com/dev-murphy/yaadchess/commit/054f18454d38fff5c92475f1efc1039f3f074494))
* add selected piece functionality ([dcc3fcd](https://github.com/dev-murphy/yaadchess/commit/dcc3fcd9ded22d6d38423f03a68704954b889aab))

### Continuous Integration

* update pyproject.toml to use [project].version instead of [commitizen].version ([20ed5d6](https://github.com/dev-murphy/yaadchess/commit/20ed5d65ccbc463ef69dff1012ebe2caee3793e8))


## [0.7.0](https://github.com/dev-murphy/yaadchess/compare/v0.6.1...v0.7.0) (2026-11-15)

### Features

* implementing moving pieces on the board ([f92d9c6](https://github.com/dev-murphy/yaadchess/commit/f92d9c697ad86af620c005d616796f2bcb19cac0))

### Miscellaneous

* resolve merge conflict ([054f184](https://github.com/dev-murphy/yaadchess/commit/054f18454d38fff5c92475f1efc1039f3f074494))
* add selected piece functionality ([dcc3fcd](https://github.com/dev-murphy/yaadchess/commit/dcc3fcd9ded22d6d38423f03a68704954b889aab))

### Continuous Integration

* update pyproject.toml to use [project].version instead of [commitizen].version ([20ed5d6](https://github.com/dev-murphy/yaadchess/commit/20ed5d65ccbc463ef69dff1012ebe2caee3793e8))

## [0.6.1](https://github.com/dev-murphy/yaadchess/releases/tag/v0.6.1) (2026-11-14)

### Code Refactors

* update app name to just chess ([db61361](https://github.com/dev-murphy/yaadchess/commit/db613617a7716e87edb579940a25baa795c3ba8d))


## [0.6.1](https://github.com/dev-murphy/yaadchess/compare/v0.6.0...v0.6.1) (2026-11-14)

### Code Refactors

* update app name to just chess ([db61361](https://github.com/dev-murphy/yaadchess/commit/db613617a7716e87edb579940a25baa795c3ba8d))

## [0.6.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.6.0) (2026-11-13)

### Features

* add basic drag function to piece component ([30be0e3](https://github.com/dev-murphy/yaadchess/commit/30be0e3db983e995b8c4edcebc444e33a90a95ac))
* implement function to place pieces on the board based on FEN notation ([2da0333](https://github.com/dev-murphy/yaadchess/commit/2da0333194e0dc9e2678440b315a5fb014757289))

### Code Refactors

* made chess board a fixed width and height ([24a0fde](https://github.com/dev-murphy/yaadchess/commit/24a0fdea3d938153995cdd4a14412a734e80cd78))
* update piece types to use FEN notation ([f4ca17d](https://github.com/dev-murphy/yaadchess/commit/f4ca17df23c6dc1d6e9753f8f8f25a6705a7dca1))

### Documentation

* update README to include scripts folder ([86666e3](https://github.com/dev-murphy/yaadchess/commit/86666e3912fcce7367b280d069b94e8db9d58488))
* add MIT license ([193e4cb](https://github.com/dev-murphy/yaadchess/commit/193e4cbbf6290bf766aedf3ab2162acb2e8f03b6))

### Miscellaneous

* prevent window from resizing and add comments ([40d61aa](https://github.com/dev-murphy/yaadchess/commit/40d61aac41757d05cba06bf9caa9b51c3d178c65))


## [0.6.0](https://github.com/dev-murphy/yaadchess/compare/v0.5.0...v0.6.0) (2026-11-13)

### Features

* add basic drag function to piece component ([30be0e3](https://github.com/dev-murphy/yaadchess/commit/30be0e3db983e995b8c4edcebc444e33a90a95ac))
* implement function to place pieces on the board based on FEN notation ([2da0333](https://github.com/dev-murphy/yaadchess/commit/2da0333194e0dc9e2678440b315a5fb014757289))

### Code Refactors

* made chess board a fixed width and height ([24a0fde](https://github.com/dev-murphy/yaadchess/commit/24a0fdea3d938153995cdd4a14412a734e80cd78))
* update piece types to use FEN notation ([f4ca17d](https://github.com/dev-murphy/yaadchess/commit/f4ca17df23c6dc1d6e9753f8f8f25a6705a7dca1))

### Documentation

* update README to include scripts folder ([86666e3](https://github.com/dev-murphy/yaadchess/commit/86666e3912fcce7367b280d069b94e8db9d58488))
* add MIT license ([193e4cb](https://github.com/dev-murphy/yaadchess/commit/193e4cbbf6290bf766aedf3ab2162acb2e8f03b6))

### Miscellaneous

* prevent window from resizing and add comments ([40d61aa](https://github.com/dev-murphy/yaadchess/commit/40d61aac41757d05cba06bf9caa9b51c3d178c65))

## [0.5.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.5.0) (2026-11-13)

### Features

* implement bitboard utility class ([ecaf234](https://github.com/dev-murphy/yaadchess/commit/ecaf234d1859f9c291232f16d1016afe5d563d2c))
* refactor to handle dev and production version of the app ([ed6cbc6](https://github.com/dev-murphy/yaadchess/commit/ed6cbc610183a6dd00015f8612f42c2afb1e11df))
* create scripts folder ([4349b18](https://github.com/dev-murphy/yaadchess/commit/4349b1810bcaad29c4da2de34488b9e6d5300e29))
* add second chess piece set to app ([315ee3c](https://github.com/dev-murphy/yaadchess/commit/315ee3ca2c46a6923a6231daaf551619b5aaa1e2))

### Bug Fixes

* disable erasableSyntaxOnly field ([d42cfb8](https://github.com/dev-murphy/yaadchess/commit/d42cfb8eda22c431cda0b30a609c43a065358bfe))
* remove unused yarn.lock ([6998fa5](https://github.com/dev-murphy/yaadchess/commit/6998fa54df68c30fc1ffb862021cc8a1131bbcc8))

### Code Refactors

* use base_url in getPiece image function ([1ba95aa](https://github.com/dev-murphy/yaadchess/commit/1ba95aa1d058fc4531454d30709fa3601deb008a))

### Miscellaneous

* add build config for pywebview production build ([17a9405](https://github.com/dev-murphy/yaadchess/commit/17a9405f2d42278b9336a35edd0def8036ce0c74))


## [0.5.0](https://github.com/dev-murphy/yaadchess/compare/v0.4.0...v0.5.0) (2026-11-13)

### Features

* implement bitboard utility class ([ecaf234](https://github.com/dev-murphy/yaadchess/commit/ecaf234d1859f9c291232f16d1016afe5d563d2c))
* refactor to handle dev and production version of the app ([ed6cbc6](https://github.com/dev-murphy/yaadchess/commit/ed6cbc610183a6dd00015f8612f42c2afb1e11df))
* create scripts folder ([4349b18](https://github.com/dev-murphy/yaadchess/commit/4349b1810bcaad29c4da2de34488b9e6d5300e29))
* add second chess piece set to app ([315ee3c](https://github.com/dev-murphy/yaadchess/commit/315ee3ca2c46a6923a6231daaf551619b5aaa1e2))

### Bug Fixes

* disable erasableSyntaxOnly field ([d42cfb8](https://github.com/dev-murphy/yaadchess/commit/d42cfb8eda22c431cda0b30a609c43a065358bfe))
* remove unused yarn.lock ([6998fa5](https://github.com/dev-murphy/yaadchess/commit/6998fa54df68c30fc1ffb862021cc8a1131bbcc8))

### Code Refactors

* use base_url in getPiece image function ([1ba95aa](https://github.com/dev-murphy/yaadchess/commit/1ba95aa1d058fc4531454d30709fa3601deb008a))

### Miscellaneous

* add build config for pywebview production build ([17a9405](https://github.com/dev-murphy/yaadchess/commit/17a9405f2d42278b9336a35edd0def8036ce0c74))

## [0.4.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.4.0) (2026-11-12)

### Features

* create Board component ([49e7241](https://github.com/dev-murphy/yaadchess/commit/49e72410e87f26611a36283e6a23c8d125cc6456))
* update pinia store to initialize board UI (doesn't include pieces) ([e59621a](https://github.com/dev-murphy/yaadchess/commit/e59621a580658eedcb3a1d0f206c72c4ec7e47d4))
* create Piece component ([0bf5cf5](https://github.com/dev-murphy/yaadchess/commit/0bf5cf5ff0e9a5759c12e014c49dbc734ef907a8))
* add basic types for piece information and board UI ([cc68994](https://github.com/dev-murphy/yaadchess/commit/cc6899474572dacd62226ee070bc7ab81ebab728))
* add first piece set to app ([7682d4c](https://github.com/dev-murphy/yaadchess/commit/7682d4cd258247cbe6671898663d8f17ba00eb34))

### Documentation

* update README with basic project information ([9f3da6c](https://github.com/dev-murphy/yaadchess/commit/9f3da6c44714a7f914631f13dc086a203b98fd14))

### Miscellaneous

* ensure elements stack on top of each other ([56072bc](https://github.com/dev-murphy/yaadchess/commit/56072bccd6ee9181552fb19c3105d5636e7b66a5))
* create helper function to get piece image ([4dcdcc6](https://github.com/dev-murphy/yaadchess/commit/4dcdcc6ee9af995f889361a9ec82480ff09325f8))
* auto-gen component types ([6d07a0c](https://github.com/dev-murphy/yaadchess/commit/6d07a0cb21ec5e5904417432663fe57942f7e780))


## [0.4.0](https://github.com/dev-murphy/yaadchess/compare/v0.3.2...v0.4.0) (2026-11-12)

### Features

* create Board component ([49e7241](https://github.com/dev-murphy/yaadchess/commit/49e72410e87f26611a36283e6a23c8d125cc6456))
* update pinia store to initialize board UI (doesn't include pieces) ([e59621a](https://github.com/dev-murphy/yaadchess/commit/e59621a580658eedcb3a1d0f206c72c4ec7e47d4))
* create Piece component ([0bf5cf5](https://github.com/dev-murphy/yaadchess/commit/0bf5cf5ff0e9a5759c12e014c49dbc734ef907a8))
* add basic types for piece information and board UI ([cc68994](https://github.com/dev-murphy/yaadchess/commit/cc6899474572dacd62226ee070bc7ab81ebab728))
* add first piece set to app ([7682d4c](https://github.com/dev-murphy/yaadchess/commit/7682d4cd258247cbe6671898663d8f17ba00eb34))

### Documentation

* update README with basic project information ([9f3da6c](https://github.com/dev-murphy/yaadchess/commit/9f3da6c44714a7f914631f13dc086a203b98fd14))

### Miscellaneous

* ensure elements stack on top of each other ([56072bc](https://github.com/dev-murphy/yaadchess/commit/56072bccd6ee9181552fb19c3105d5636e7b66a5))
* create helper function to get piece image ([4dcdcc6](https://github.com/dev-murphy/yaadchess/commit/4dcdcc6ee9af995f889361a9ec82480ff09325f8))
* auto-gen component types ([6d07a0c](https://github.com/dev-murphy/yaadchess/commit/6d07a0cb21ec5e5904417432663fe57942f7e780))

## [0.3.2](https://github.com/dev-murphy/yaadchess/releases/tag/v0.3.2) (2026-11-12)

### Bug Fixes

* prevent repeated CHANGELOG heading ([df5a423](https://github.com/dev-murphy/yaadchess/commit/df5a423c4f9472a6f8f80d73e4e37d1eac109654))


## [0.3.2](https://github.com/dev-murphy/yaadchess/compare/v0.3.1...v0.3.2) (2026-11-12)

### Bug Fixes

* prevent repeated CHANGELOG heading ([df5a423](https://github.com/dev-murphy/yaadchess/commit/df5a423c4f9472a6f8f80d73e4e37d1eac109654))

## [0.3.1](https://github.com/dev-murphy/yaadchess/releases/tag/v0.3.1) (2026-11-12)

### Bug Fixes

* resolve issue with CHANGELOG template and CHANGELOG ([1954e82](https://github.com/dev-murphy/yaadchess/commit/1954e82e38a080329f365ddbe1795eb3b842669e))


## [0.3.1](https://github.com/dev-murphy/yaadchess/compare/v0.3.0...v0.3.1) (2026-11-12)

### Bug Fixes

* resolve issue with CHANGELOG template and CHANGELOG ([1954e82](https://github.com/dev-murphy/yaadchess/commit/1954e82e38a080329f365ddbe1795eb3b842669e))

## [0.3.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.3.0) (2026-11-12)

### Features

* add basic package deps for UI project ([c865fab](https://github.com/dev-murphy/yaadchess/commit/c865fab665e96ca07ba1cd7c0a56521a37860b97))
* add vite project for UI ([3fe3afb](https://github.com/dev-murphy/yaadchess/commit/3fe3afbe3e7313235690348ed771cd9139dbae48))
* add script to run both projects ([88ff599](https://github.com/dev-murphy/yaadchess/commit/88ff599031db271f8f92914cded9403115b5c336))
* install and setup pywebview ([90f86a2](https://github.com/dev-murphy/yaadchess/commit/90f86a275c418ff8da206f82de15c6a3c2cd9f06))

### Code Refactors

* remove public folder ([e0c35e4](https://github.com/dev-murphy/yaadchess/commit/e0c35e411cf05e9b4f1b0ec55c6fa1d90e221723))
* update code structure ([5dca1bd](https://github.com/dev-murphy/yaadchess/commit/5dca1bd12dae5da279a1a9f97e77c841c73aad30))

### Miscellaneous

* add node specific config to global gitignore file ([8f53e2b](https://github.com/dev-murphy/yaadchess/commit/8f53e2b5354c9d1d7dcdc0c6552f383d501c2381))


## [0.3.0](https://github.com/dev-murphy/yaadchess/compare/v0.2.2...v0.3.0) (2026-11-12)

### Features

* add basic package deps for UI project ([c865fab](https://github.com/dev-murphy/yaadchess/commit/c865fab665e96ca07ba1cd7c0a56521a37860b97))
* add vite project for UI ([3fe3afb](https://github.com/dev-murphy/yaadchess/commit/3fe3afbe3e7313235690348ed771cd9139dbae48))
* add script to run both projects ([88ff599](https://github.com/dev-murphy/yaadchess/commit/88ff599031db271f8f92914cded9403115b5c336))
* install and setup pywebview ([90f86a2](https://github.com/dev-murphy/yaadchess/commit/90f86a275c418ff8da206f82de15c6a3c2cd9f06))

### Code Refactors

* remove public folder ([e0c35e4](https://github.com/dev-murphy/yaadchess/commit/e0c35e411cf05e9b4f1b0ec55c6fa1d90e221723))
* update code structure ([5dca1bd](https://github.com/dev-murphy/yaadchess/commit/5dca1bd12dae5da279a1a9f97e77c841c73aad30))

### Miscellaneous

* add node specific config to global gitignore file ([8f53e2b](https://github.com/dev-murphy/yaadchess/commit/8f53e2b5354c9d1d7dcdc0c6552f383d501c2381))

## [0.2.2](https://github.com/dev-murphy/yaadchess/releases/tag/v0.2.2) (2026-11-12)

### Bug Fixes

* **release:** push annotated tags and use custom commitizen rules ([dfee478](https://github.com/dev-murphy/yaadchess/commit/dfee478af549e3c9c6f70953822a1434c2e9d461))


## [0.2.2](https://github.com/dev-murphy/yaadchess/compare/v0.2.1...v0.2.2) (2026-11-12)

### Bug Fixes

* **release:** push annotated tags and use custom commitizen rules ([dfee478](https://github.com/dev-murphy/yaadchess/commit/dfee478af549e3c9c6f70953822a1434c2e9d461))

## [0.2.1](https://github.com/dev-murphy/yaadchess/releases/tag/v0.2.1) (2026-11-11)

### Bug Fixes

* resolve all issues with CHANGELOG template ([6136968](https://github.com/dev-murphy/yaadchess/commit/6136968a6754bd02eb071ae5f9d3e5682ac568c3))
* update syntax in CHANGELOG template file ([717989a](https://github.com/dev-murphy/yaadchess/commit/717989a00ef623521f7df19e7b08625a3e3ea242))
* use correct field name for commitizen config ([07fe4e9](https://github.com/dev-murphy/yaadchess/commit/07fe4e988a2d6170a3a55920b66dd2f62488f0ec))

### Code Refactors

* update formatting the changelog file ([c8e6e86](https://github.com/dev-murphy/yaadchess/commit/c8e6e8634b88215580dc0506ebb8df00fd387cd6))


## [0.2.1](https://github.com/dev-murphy/yaadchess/compare/v0.2.0...v0.2.1) (2026-11-12)

### Bug Fixes

* resolve all issues with CHANGELOG template ([6136968](https://github.com/dev-murphy/yaadchess/commit/6136968a6754bd02eb071ae5f9d3e5682ac568c3))
* update syntax in CHANGELOG template file ([717989a](https://github.com/dev-murphy/yaadchess/commit/717989a00ef623521f7df19e7b08625a3e3ea242))
* use correct field name for commitizen config ([07fe4e9](https://github.com/dev-murphy/yaadchess/commit/07fe4e988a2d6170a3a55920b66dd2f62488f0ec))

### Code Refactors

* update formatting the changelog file ([c8e6e86](https://github.com/dev-murphy/yaadchess/commit/c8e6e8634b88215580dc0506ebb8df00fd387cd6))

## [0.2.0](https://github.com/dev-murphy/yaadchess/releases/tag/v0.2.0) (2026-11-11)

### Features

* add automated release github action ([73e89a1](https://github.com/dev-murphy/yaadchess/commit/73e89a19318654ff5d202aeb6d59742da93183a3))
* add uv, ruff and pytest packages ([5301b27](https://github.com/dev-murphy/yaadchess/commit/5301b27a9b9e35eaff24130ae27de16f589db144))
* add .gitignore file ([43a7eb3](https://github.com/dev-murphy/yaadchess/commit/43a7eb394a18747b509608ae47e84c9413998ca6))

